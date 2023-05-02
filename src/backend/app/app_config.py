import os

class Config:
    COUCHDB_HOST = os.environ.get('COUCHDB_HOST', 'localhost')
    COUCHDB_PORT = os.environ.get('COUCHDB_PORT', '5984')
    COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME', 'admin')
    COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD', 'admin')
    COUCHDB_DATABASES = os.environ.get('COUCHDB_DATABASES', {'test'})
    
    if COUCHDB_USERNAME and COUCHDB_PASSWORD:
        COUCHDB_URL = f"http://{COUCHDB_USERNAME}:{COUCHDB_PASSWORD}@{COUCHDB_HOST}:{COUCHDB_PORT}/"