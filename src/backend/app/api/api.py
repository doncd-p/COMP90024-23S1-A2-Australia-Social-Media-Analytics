from flask import Flask, jsonify, request
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
        limit = request.args.get('limit', default=100, type=int)
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True, limit=limit)
        texts = []
        for r in results:
            try:
                text = r['doc']['text']
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
        limit = request.args.get('limit', default=100, type=int)
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True, limit=limit)
        sentiments = []
        for r in results:
            try:
                sentiment = {
                    "neg_score": r['doc']['neg_score'],
                    "neu_score": r['doc']['neu_score'],
                    "pos_score": r['doc']['pos_score'],
                    "compound_score": r['doc']['compound_score'],
                    "sentiment": r['doc']['sentiment']
                }
                sentiments.append(sentiment)
            except KeyError:
                continue
        return jsonify(sentiments)

class GetAllElectorates(Resource):
    def get(self, db_name):
        """
        Retrieve all electrorate data from a specified database in CouchDB.

        Args:
            db_name (str): The name of the database to retrieve data from.

        Returns:
            A JSON response containing an array of electrorate data.
        """
        limit = request.args.get('limit', default=100, type=int)
        db = client.get_db(db_name)
        results = db.view('_all_docs', include_docs=True, limit=limit)
        electorates = []
        for r in results:
            try:
                electorate = r['doc']['electorate']
                electorates.append(electorate)
            except KeyError:
                continue
        return jsonify(electorates)

