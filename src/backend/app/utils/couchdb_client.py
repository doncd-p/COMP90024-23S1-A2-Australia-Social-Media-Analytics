import couchdb
import requests
import json
from ..app_config import Config

class CouchDBClient:
    def __init__(self):
        self.server_url, self.server = self.connect_to_couchdb()
        self.databases = {}
        
        for db_name in self.server:
            try:
                db = self.server[db_name]
                self.databases[db_name] = db
            except couchdb.ResourceNotFound:
                pass
                
    def connect_to_couchdb(self):
        for url in Config.couchdb_urls():
            try:
                server = couchdb.Server(url)
                # Try to access the server to check if it's up
                server.version() 
                return url, server
            except:
                # If the server is down, an exception will be raised
                # and the next server in the list will be tried.
                pass
        raise Exception("No available CouchDB servers found")
    
    def find_in_partition(self, db_name, partition_key, query):
        if db_name not in self.databases:
            raise ValueError(f"Unknown database: {db_name}")

        url = f"{self.server_url}{db_name}/_partition/{partition_key}/_find"
        response = requests.post(url, data=json.dumps(query), headers={"Content-Type": "application/json"})

        if response.status_code != 200:
            raise Exception(f"Error executing query: {response.content}")

        return response.json()

    def get_db(self, db_name):
        if db_name not in self.databases:
            raise ValueError(f"Unknown database: {db_name}")

        return self.databases[db_name]

client = CouchDBClient()