import os


class Config:
    BASE_URL = os.environ.get('BASE_URL', 'http://localhost:8080')
    COUCHDB_HOSTS = os.environ.get(
        'COUCHDB_HOSTS').split(',')
    COUCHDB_PORT = os.environ.get('COUCHDB_PORT', '5984')
    COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME', 'group9_admin')
    COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD', 'group9_H1')

    @classmethod
    def couchdb_urls(cls):
        return [f"http://{cls.COUCHDB_USERNAME}:{cls.COUCHDB_PASSWORD}@{host}:{cls.COUCHDB_PORT}/" for host in cls.COUCHDB_HOSTS]