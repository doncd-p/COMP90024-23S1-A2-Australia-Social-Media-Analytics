import couchdb
from ..app_config import Config

class CouchDBClient:
    def __init__(self):
        self.servers = [couchdb.Server(url) for url in Config.couchdb_urls()]
        self.databases = {}

        for server in self.servers:
            for db_name in Config.COUCHDB_DATABASES:
                try:
                    db = server[db_name]
                    self.databases[db_name] = db
                except couchdb.ResourceNotFound:
                    pass

    def get_db(self, db_name):
        if db_name not in self.databases:
            raise ValueError(f"Unknown database: {db_name}")

        return self.databases[db_name]
