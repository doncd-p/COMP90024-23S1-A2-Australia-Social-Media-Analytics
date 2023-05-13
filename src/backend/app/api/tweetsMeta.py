from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import client

class TweetsMeta(Resource):
    def get(self):
        db = client.get_db('tweet_database')
        view = db.view('_design/political/_view/political')

        result = next(iter(view), None)
        if result is None:
            response = jsonify(
                code=404,
                msg='No data found',
                data={}
            )
            response.status_code = 404
            return response

        tweets_meta = {
            'sum': result.value['sum'],
            'count': result.value['count'],
            'mean': result.value['sum'] / result.value['count']
        }

        response = jsonify(
            code=200,
            msg='ok',
            data=tweets_meta
        )
        response.status_code = 200
        return response