from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import client

class TopPositiveTweets(Resource):
    def get(self):
        top_k = int(request.args.get('num', 5))
        electorate = request.args.get('electorate')
                
        electorate = electorate.lower()
        electorate = electorate[0].upper() + electorate[1:]
        
        if top_k > 5:
            response = jsonify(
                code=500,
                msg='Limit number of tweets within 5',
                data={}
            )
            response.status_code = 500
            return response

        if not electorate:
            response = jsonify(
                code=400,
                msg="Electorate is required",
                data={},
            ), 400
            return response

        query = {
            "selector": {
                "is_political": {
                    "$eq": 1
                }
            },
            "sort": [
                {
                    "pos_score": "desc"
                }
            ],
            "limit": top_k
        }

        try:
            result = client.find_in_partition('tweet_database__electorate', electorate, query)
        except Exception as e:
            response = jsonify(
                code=500,
                msg="Error occurred: " + str(e),
                data={},
            )
            response.status_code = 500
            return response

        cleaned_tweet_list = []
        for item in result['docs']:
            cleaned_tweet = {}
            cleaned_tweet['author'] = item['author_id']
            if ':' not in item['_id']:
                cleaned_tweet['tweet_id'] = item['_id']
            else:
                cleaned_tweet['tweet_id'] = item['_id'].split(':')[1]
            cleaned_tweet['date'] = item['date']
            cleaned_tweet['text'] = item['text']
            cleaned_tweet['pos_score'] = item['pos_score']
            cleaned_tweet['compound_score'] = item['compound_score']

            cleaned_tweet_list.append(cleaned_tweet)

        response = jsonify(
            code=200,
            msg="ok",
            data=cleaned_tweet_list,
        )
        return response

class TopNegativeTweets(Resource):
    def get(self):
        top_k = int(request.args.get('num', 5))
        electorate = request.args.get('electorate')
        
        db = client.get_db('tweet_database__electorate')
        
        if top_k > 5:
            response = jsonify(
                code=500,
                msg='Limit number of tweets within 5',
                data={}
            )
            response.status_code = 500
            return response

        if not electorate:
            response = jsonify(
                code=400,
                msg="Electorate is required",
                data={},
            )
            response.status_code = 400
            return response

        query = {
            "selector": {
                "is_political": {
                    "$eq": 1
                }
            },
            "sort": [
                {
                    "neg_score": "desc"
                }
            ],
            "limit": top_k
        }

        try:
            result = db.find(query)
        except Exception as e:
            response = jsonify(
                code=500,
                msg="Error occurred: " + str(e),
                data={},
            )
            response.status_code = 500
            return response

        cleaned_tweet_list = []
        for item in result:
            cleaned_tweet = {}
            cleaned_tweet['author'] = item['author_id']
            if ':' not in item['_id']:
                cleaned_tweet['tweet_id'] = item['_id']
            else:
                cleaned_tweet['tweet_id'] = item['_id'].split(':')[1]
            cleaned_tweet['date'] = item['date']
            cleaned_tweet['text'] = item['text']
            cleaned_tweet['neg_score'] = item['neg_score']
            cleaned_tweet['compound_score'] = item['compound_score']

            cleaned_tweet_list.append(cleaned_tweet)

        response = jsonify(
            code=200,
            msg="ok",
            data=cleaned_tweet_list,
        )
        response.status_code = 200
        return response