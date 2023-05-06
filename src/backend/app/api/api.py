from flask import Flask, jsonify
from flask_restful import Api, Resource
from app.utils.couchdb_client import CouchDBClient

app = Flask(__name__)
api = Api(app)
client = CouchDBClient()

class GetAllTexts(Resource):
    def get(self, db_name):
        """
        Retrieve all text data from a specified database in CouchDB.

        Args:
            db_name (str): The name of the database to retrieve data from.

        Returns:
            A JSON response containing an array of text data.
        """
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True)
        texts = []
        for r in results:
            try:
                text = r['doc']['data']['text']
                texts.append(text)
            except KeyError:
                continue
        return jsonify(texts)

class GetAllSentiments(Resource):
    def get(self, db_name):
        """
        Retrieve all sentiment data from a specified database in CouchDB.

        Args:
            db_name (str): The name of the database to retrieve data from.

        Returns:
            A JSON response containing an array of sentiment data.
        """
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True)
        sentiments = []
        for r in results:
            try:
                sentiment = r['doc']['data']['sentiment']
                sentiments.append(sentiment)
            except KeyError:
                continue
        return jsonify(sentiments)

class GetAllBBox(Resource):
    def get(self, db_name):
        """
        Retrieve all bbox data from a specified database in CouchDB.

        Args:
            db_name (str): The name of the database to retrieve data from.

        Returns:
            A JSON response containing an array of bbox data.
        """
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True)
        bboxes = []
        for r in results:
            try:
                bbox = r['doc']['includes']['places'][0]['geo']['bbox']
                bboxes.append(bbox)
            except KeyError:
                continue
        return jsonify(bboxes)
