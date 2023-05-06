import os

class Config:
    COUCHDB_HOSTS = os.environ.get('COUCHDB_HOSTS', 'localhost').split(',')
    COUCHDB_PORT = os.environ.get('COUCHDB_PORT', '5984')
    COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME', 'admin')
    COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD', 'admin')
    COUCHDB_DATABASES = os.environ.get('COUCHDB_DATABASES', 'db1,db2,test').split(',')
    
    @classmethod
    def couchdb_urls(cls):
        return [f"http://{cls.COUCHDB_USERNAME}:{cls.COUCHDB_PASSWORD}@{host}:{cls.COUCHDB_PORT}/" for host in cls.COUCHDB_HOSTS]