from flask_restful import Api
from .api import GetAllTexts, GetAllSentiments, GetAllBBox

def init_api(app):
    """
    Initialize the API, adding all routes to the Flask app.

    Args:
        app (Flask): The Flask app
    """
    
    api = Api(app, prefix='/api')
    api.add_resource(GetAllTexts, '/<string:db_name>/all_texts')
    api.add_resource(GetAllSentiments, '/<string:db_name>/all_sentiments')
    api.add_resource(GetAllBBox, '/<string:db_name>/all_bboxs')
