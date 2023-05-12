import os

class Config:
    COUCHDB_HOSTS = os.environ.get('COUCHDB_HOSTS', '172.26.133.251').split(',')
    COUCHDB_PORT = os.environ.get('COUCHDB_PORT', '5984')
    COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME', 'group9_admin')
    COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD', 'group9_H1')
    COUCHDB_DATABASES = os.environ.get('COUCHDB_DATABASES', 'twitter_database').split(',')
    
    @classmethod
    def couchdb_urls(cls):
        return [f"http://{cls.COUCHDB_USERNAME}:{cls.COUCHDB_PASSWORD}@{host}:{cls.COUCHDB_PORT}/" for host in cls.COUCHDB_HOSTS]