from .db import init_db

def init_utils(app):
    """
    Initialize the API, adding all the helpers to the Flask app.

    Args:
        app (Flask): The Flask app
    """
    global _couch

    # Initialize the database connections
    _couch = {}
    db_names = app.config.get('COUCHDB_DATABASES')
    for name in db_names:
        _couch[name] = init_db(app, name)

def get_couch(db_name):
    if db_name not in _couch:
        raise Exception(f"CouchDB '{db_name}' not initialized")
    return _couch[db_name]