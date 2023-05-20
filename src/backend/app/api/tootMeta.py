from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import CouchDBClient


class TootMeta(Resource):
    def get(self):
        client = CouchDBClient()
        db = client.get_db('toot_database')
        view = db.view('_design/partial_match/_view/partial_match')

        result = next(iter(view), None)
        if result is None:
            response = jsonify(
                code=404,
                msg='No data found',
                data={}
            )
            response.status_code = 404
            return response

        toot_meta = {
            'sum': result.value['count'] - result.value['sum'],
            'count': result.value['count'],
            'mean': 1 - result.value['sum'] / result.value['count']
        }

        response = jsonify(
            code=200,
            msg='ok',
            data=toot_meta
        )
        response.status_code = 200
        return response
