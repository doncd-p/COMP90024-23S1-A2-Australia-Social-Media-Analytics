import couchdb
import requests
import json
import random
from ..app_config import Config


class CouchDBClient:
    def __init__(self):
        self.servers = self.connect_to_couchdb()

    def connect_to_couchdb(self):
        # Try to connect to each CouchDB server in the configuration
        servers = []
        for url in Config.couchdb_urls():
            try:
                server = couchdb.Server(url)
                # Try to access the server to check if it's up
                server.version()
                servers.append((url, server))
            except:
                # If the server is down, an exception will be raised
                # and the next server in the list will be tried.
                pass
        if not servers:
            raise Exception("No available CouchDB servers found")
        return servers

    def find_in_partition(self, db_name, partition_key, query):
        # Choose a random server and find the corresponding database
        server_url, server = random.choice(self.servers)
        remote_db_name = self.get_remote_db_name(db_name, server)

        url = f"{server_url}{remote_db_name}/_partition/{partition_key}/_find"
        response = requests.post(url, data=json.dumps(query), headers={
                                 "Content-Type": "application/json"})

        if response.status_code != 200:
            raise Exception(f"Error executing query: {response.content}")

        return response.json()

    def get_db(self, db_name):
        # Choose a random server and find the corresponding database
        server_url, server = random.choice(self.servers)
        remote_db_name = self.get_remote_db_name(db_name, server)
        try:
            db = server[remote_db_name]
        except couchdb.ResourceNotFound:
            raise ValueError(f"Unknown database: {db_name}")
        return db

    def get_remote_db_name(self, db_name, server):
        # Find the best matching database in the given server for CouchDB replicate renaming issue
        best_match = None
        for remote_db_name in server:
            if db_name in remote_db_name:
                if best_match is None or len(remote_db_name) < len(best_match):
                    best_match = remote_db_name
        if best_match is not None:
            return best_match
        else:
            raise ValueError(f"Unknown database: {db_name}")


client = CouchDBClient()
