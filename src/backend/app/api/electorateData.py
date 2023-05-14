from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import client


class ElectorateData(Resource):
    def get(self):
        electorate_filter = request.args.get('electorate')

        db = client.get_db('sudo_electorate')

        # If a specific electorate has been requested, filter the results
        if electorate_filter:
            try:
                doc = db.get(electorate_filter)
                # Remove polygonData from the document
                doc.pop('polygonData', None)
                response = jsonify(
                    code=200,
                    msg="ok",
                    data=doc,
                )
                response.status_code = 200
                return response
            except:
                response = jsonify(
                    code=404,
                    msg="Electorate not found",
                    data={},
                )
                response.status_code = 404
                return response
        else:
            response = jsonify(
                code=400,
                msg="No electorate provided",
                data={},
            )
            response.status_code = 400
            return response


class ElectorateGeoData(Resource):
    def get(self):
        db = client.get_db('geo_electorate')

        view = db.view('_all_docs', limit=1, include_docs=True)

        for row in view:
            doc = row['doc']
            break

        if doc:
            response = jsonify(
                code=200,
                msg="ok",
                data=doc
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                code=404,
                msg="Document not found",
                data={}
            )
            response.status_code = 404
            return response
