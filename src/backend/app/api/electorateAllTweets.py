from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import client


class DateSentimentAll(Resource):
    def get(self):
        startdate = request.args.get('startdate')
        enddate = request.args.get('enddate')
        electorate_filter = request.args.get('electorate')

        db = client.get_db('tweet_database')
        view = db.view('_design/date/_view/date_electorate__nsentiment',
                       group=True, startkey=[startdate], endkey=[enddate])

        # Process data
        electorate_n_sent = {}
        for item in view:
            electorate = item.key[1]
            if electorate not in electorate_n_sent:
                electorate_n_sent[electorate] = {
                    'num_pos_tweets': 0,
                    'num_neu_tweets': 0,
                    'num_neg_tweets': 0
                }

            sentiment_keys = ['num_pos_tweets',
                              'num_neu_tweets', 'num_neg_tweets']
            for j in range(3):
                electorate_n_sent[electorate][sentiment_keys[j]
                                              ] += item.value[j]['sum']

        # If a specific electorate has been requested, filter the results
        if electorate_filter:
            if electorate_filter in electorate_n_sent:
                response = jsonify(
                    code=200,
                    msg="ok",
                    data={
                        electorate_filter: electorate_n_sent[electorate_filter]},
                )
                response.status_code = 200
                return response
            else:
                response = jsonify(
                    code=404, err="Electorate not found", data={})
                response.status_code = 404
                return response

        response = jsonify(code=200, msg="ok", data=electorate_n_sent)
        response.status_code = 200
        return response


class DateAvgSentimentAll(Resource):
    def get(self):
        startdate = request.args.get('startdate')
        enddate = request.args.get('enddate')
        electorate_filter = request.args.get('electorate')
        range_type = request.args.get('type', 'daily')

        db = client.get_db('tweet_database')
        view = db.view('_design/date/_view/date_electorate__avgsent',
                       group=True, startkey=[startdate], endkey=[enddate])

        # Process data
        if not electorate_filter:
            electorate_avg_sent_sum_count = {}
            for item in view:
                electorate = item.key[1]
                if electorate not in electorate_avg_sent_sum_count:
                    electorate_avg_sent_sum_count[electorate] = [0, 0]

                electorate_avg_sent_sum_count[electorate][0] += item.value['sum']
                electorate_avg_sent_sum_count[electorate][1] += item.value['count']

            electorate_avg_sent = {key: {'avg_sentiment': electorate_avg_sent_sum_count[key][0]/electorate_avg_sent_sum_count[key]
                                         [1], 'num_tweets': electorate_avg_sent_sum_count[key][1]} for key in electorate_avg_sent_sum_count}

            return jsonify(
                code=200,
                msg="ok",
                data=electorate_avg_sent,
            )

        if range_type == "daily":
            daily_by_electorate_sentiment = {}
            for item in view:
                electorate = item.key[1]
                if electorate not in daily_by_electorate_sentiment:
                    daily_by_electorate_sentiment[electorate] = {}

                date = item.key[0]
                daily_by_electorate_sentiment[electorate][date] = item.value['sum'] / \
                    item.value['count']

            # If a specific electorate has been requested, filter the results
            if electorate_filter:
                if electorate_filter in daily_by_electorate_sentiment:
                    response = jsonify(
                        code=200,
                        msg="ok",
                        data=daily_by_electorate_sentiment[electorate_filter],
                    )
                    response.status_code = 200
                    return response
                else:
                    response = jsonify(
                        code=404,
                        msg="Electorate not found",
                        data={},
                    )
                    response.status_code = 404
                    return response

            response = jsonify(
                code=200,
                msg="ok",
                data=daily_by_electorate_sentiment,
            )
            response.status_code = 200
            return response

        elif range_type == "monthly":
            monthly_by_electorate_sentiment = {}
            for item in view:
                electorate = item.key[1]
                if electorate not in monthly_by_electorate_sentiment:
                    monthly_by_electorate_sentiment[electorate] = {}

                month = item.key[0][5:7]
                monthly_by_electorate_sentiment[electorate][month] = item.value['sum'] / \
                    item.value['count']

            # If a specific electorate has been requested, filter the results
            if electorate_filter:
                if electorate_filter in monthly_by_electorate_sentiment:
                    response = jsonify(
                        code=200,
                        msg="ok",
                        data=monthly_by_electorate_sentiment[electorate_filter],
                    )
                    response.status_code = 200
                    return response
                else:
                    response = jsonify(
                        code=404,
                        msg="Electorate not found",
                        data={},
                    )
                    response.status_code = 404
                    return response

            response = jsonify(
                code=200,
                msg="ok",
                data=monthly_by_electorate_sentiment,
            )
            response.status_code = 200
            return response
        else:
            response = jsonify(
                code=400,
                msg="Invalid range type. It should be either 'daily' or 'monthly'.",
                data={},
            )
            response.status_code = 400

        return response


class WeeklyAvgSentimentAll(Resource):
    def get(self):
        startweek = request.args.get('startweek')
        endweek = request.args.get('endweek')
        electorate_filter = request.args.get('electorate')

        db = client.get_db('tweet_database')
        view = db.view('_design/week/_view/week_electorate__avgsent',
                       group=True, startkey=[startweek], endkey=[endweek])

        # Process data
        if not electorate_filter:
            electorate_avg_sent_sum_count = {}
            for item in view:
                electorate = item.key[1]
                if electorate not in electorate_avg_sent_sum_count:
                    electorate_avg_sent_sum_count[electorate] = [0, 0]

                electorate_avg_sent_sum_count[electorate][0] += item.value['sum']
                electorate_avg_sent_sum_count[electorate][1] += item.value['count']

            electorate_avg_sent = {key: {'avg_sentiment': electorate_avg_sent_sum_count[key][0]/electorate_avg_sent_sum_count[key]
                                         [1], 'num_tweets': electorate_avg_sent_sum_count[key][1]} for key in electorate_avg_sent_sum_count}

            response = jsonify(
                code=200,
                msg="ok",
                data=electorate_avg_sent,
            )
            response.status_code = 200
            return response

        weekly_by_electorate_sentiment = {}
        for item in view:
            electorate = item.key[1]
            if electorate not in weekly_by_electorate_sentiment:
                weekly_by_electorate_sentiment[electorate] = {}

            week = item.key[0]

            weekly_by_electorate_sentiment[electorate][week] = item.value['sum'] / \
                item.value['count']

        # If a specific electorate has been requested, filter the results
        if electorate_filter:
            if electorate_filter in weekly_by_electorate_sentiment:
                response = jsonify(
                    code=200,
                    msg="ok",
                    data={
                        electorate_filter: weekly_by_electorate_sentiment[electorate_filter]},
                )
                response.status_code = 200
                return response
            else:
                response = jsonify(
                    code=404,
                    msg="Electorate not found",
                    data={},
                )
                response.status_code = 404
                return response

        response = jsonify(
            code=200,
            msg="ok",
            data=weekly_by_electorate_sentiment,
        )
        response.status_code = 200
        return response
