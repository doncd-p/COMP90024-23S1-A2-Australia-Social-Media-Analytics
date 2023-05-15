from flask_cors import CORS

def init_cors(app):
    """
    Initialize the API, adding all the helpers to the Flask app.

    Args:
        app (Flask): The Flask app
    """

    cors = CORS(app, supports_credentials=True)
    
