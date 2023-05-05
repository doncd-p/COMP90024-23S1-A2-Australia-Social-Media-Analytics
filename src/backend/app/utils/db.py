from couchdb import Server

def init_db(app, db_name):
    """
    Initialize the CouchDB database

    Args:
        app (Flask): The Flask app
        db_name (str): The name of the CouchDB database to connect to
    """
    couchdb_url = app.config.get('COUCHDB_URL')
    
    # Connect to the CouchDB server
    couchdb_server = Server(couchdb_url)

    # Create the database if it doesn't exist
    if db_name not in couchdb_server:
        couchdb_server.create(db_name)
        
    # Select the database
    db = couchdb_server[db_name]
    
    return db