from flask import Flask
from .utils.cors import init_cors
from .api import init_api
from .app_config import Config


def create_app():
    # Initialize the configuration of flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize all the helpers to the Flask app
    with app.app_context():
        init_cors(app)
        init_api(app)

    return app
