import couchdb
import requests
import json
from ..app_config import Config


class CouchDBClient:
    def __init__(self):
        self.server_url, self.server = self.connect_to_couchdb()
        self.databases = {}

        for remote_db_name in self.server:
            try:
                db = self.server[remote_db_name]
                self.databases[remote_db_name] = db
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
        remote_db_name = self.get_remote_db_name(db_name)

        url = f"{self.server_url}{remote_db_name}/_partition/{partition_key}/_find"
        response = requests.post(url, data=json.dumps(query), headers={
                                 "Content-Type": "application/json"})

        if response.status_code != 200:
            raise Exception(f"Error executing query: {response.content}")

        return response.json()

    def get_db(self, db_name):
        remote_db_name = self.get_remote_db_name(db_name)
        return self.databases[remote_db_name]

    def get_remote_db_name(self, db_name):
        best_match = None
        for remote_db_name in self.databases:
            if db_name in remote_db_name:
                # If this is the first match or a better match, update best_match
                if best_match is None or len(remote_db_name) < len(best_match):
                    best_match = remote_db_name
        if best_match is not None:
            return best_match
        else:
            raise ValueError(f"Unknown database: {db_name}")

    def find_original_name(self, db_name):
        # Check if any of the orginal database names is a substring of db_name
        for original_db_name in self.server:
            if original_db_name in db_name:
                return original_db_name
        return None


client = CouchDBClient()
