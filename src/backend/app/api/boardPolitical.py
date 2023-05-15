from flask import jsonify, request
from flask_restful import Resource
from app.utils.couchdb_client import client
import calendar
from datetime import datetime


class BoardDailyAvgSentimentPolitical(Resource):
    def get(self):
        try:
            startdate = request.args.get('startdate', '2022-02-10')
            enddate = request.args.get('enddate', '2022-05-21')

            # Validate date format
            try:
                start_date = datetime.strptime(startdate, '%Y-%m-%d')
                end_date = datetime.strptime(enddate, '%Y-%m-%d')
            except ValueError:
                response = jsonify(
                    code=400,
                    msg="Invalid date format. Expected format is YYYY-MM-DD.",
                    data={},
                )
                response.status_code = 400
                return response

            # Validate date order
            if startdate > enddate:
                response = jsonify(
                    code=400,
                    msg="Start date cannot be after end date.",
                    data={},
                )
                response.status_code = 400
                return response

            db = client.get_db('tweet_database')
            view = db.view('_design/date/_view/date_electorate__avgsent__pol',
                           group=True, startkey=[startdate], endkey=[enddate])

            # Process data
            daily_AUS_sentiment_sum_count = {}
            for item in view:
                date = item.key[0]
                if date not in daily_AUS_sentiment_sum_count:
                    daily_AUS_sentiment_sum_count[date] = {
                        'sum': 0, 'count': 0}

                daily_AUS_sentiment_sum_count[date]['sum'] += item.value['sum']
                daily_AUS_sentiment_sum_count[date]['count'] += item.value['count']

            daily_AUS_sentiment_list = sorted(
                [[key, daily_AUS_sentiment_sum_count[key]['sum']/daily_AUS_sentiment_sum_count[key]['count']]
                 for key in daily_AUS_sentiment_sum_count],
                key=lambda x: x[0])

            response = jsonify(
                code=200,
                msg="ok",
                data=daily_AUS_sentiment_list,
            )
            response.status_code = 200
            return response

        except Exception as e:
            response = jsonify(
                code=500,
                msg="Error occurred: " + str(e),
                data={},
            )
            response.status_code = 500
            return response


class BoardWeeklyAvgSentimentPolitical(Resource):
    def get(self):
        try:
            startweek = int(request.args.get('startweek', -15))
            endweek = int(request.args.get('endweek', 0)) + 1

            # Validate date order
            if startweek > endweek:
                response = jsonify(
                    code=400,
                    msg="Start week cannot be after end week.",
                    data={},
                )
                response.status_code = 400
                return response

            db = client.get_db('tweet_database')
            view = db.view('_design/week/_view/week_electorate__avgsent__pol',
                           group=True, startkey=[startweek], endkey=[endweek])

            # Process data
            weekly_AUS_sentiment_sum_count = {}
            for item in view:
                week = item.key[0]
                if week not in weekly_AUS_sentiment_sum_count:
                    weekly_AUS_sentiment_sum_count[week] = {
                        'sum': 0, 'count': 0}

                weekly_AUS_sentiment_sum_count[week]['sum'] += item.value['sum']
                weekly_AUS_sentiment_sum_count[week]['count'] += item.value['count']

            weekly_AUS_sentiment_list = sorted(
                [[key, weekly_AUS_sentiment_sum_count[key]['sum']/weekly_AUS_sentiment_sum_count[key]['count']]
                 for key in weekly_AUS_sentiment_sum_count],
                key=lambda x: x[0])

            response = jsonify(
                code=200,
                msg="ok",
                data=weekly_AUS_sentiment_list,
            )
            response.status_code = 200
            return response

        except Exception as e:
            response = jsonify(
                code=500,
                msg="Error occurred: " + str(e),
                data={},
            )
            response.status_code = 500
            return response


class BoardMonthlyAvgSentimentPolitical(Resource):
    def get(self):
        try:
            startdate = request.args.get('startdate', '2022-02-10')
            enddate = request.args.get('enddate', '2022-05-21')

            # Validate date format
            try:
                start_date = datetime.strptime(startdate, '%Y-%m-%d')
                end_date = datetime.strptime(enddate, '%Y-%m-%d')
            except ValueError:
                response = jsonify(
                    code=400,
                    msg="Invalid date format. Expected format is YYYY-MM-DD.",
                    data={},
                )
                response.status_code = 400
                return response

            # Validate date order
            if startdate > enddate:
                response = jsonify(
                    code=400,
                    msg="Start date cannot be after end date.",
                    data={},
                )
                response.status_code = 400
                return response

            db = client.get_db('tweet_database')
            view = db.view('_design/date/_view/date_electorate__avgsent__pol',
                           group=True, startkey=[startdate], endkey=[enddate])

            # Process data
            monthly_AUS_sentiment_sum_count = {}
            for item in view:
                month = item.key[0][5:7]
                month_name = calendar.month_name[int(month)]
                if month_name not in monthly_AUS_sentiment_sum_count:
                    monthly_AUS_sentiment_sum_count[month_name] = {
                        'sum': 0, 'count': 0}

                monthly_AUS_sentiment_sum_count[month_name]['sum'] += item.value['sum']
                monthly_AUS_sentiment_sum_count[month_name]['count'] += item.value['count']

            monthly_AUS_sentiment_list = sorted(
                [[key, monthly_AUS_sentiment_sum_count[key]['sum']/monthly_AUS_sentiment_sum_count[key]['count']]
                 for key in monthly_AUS_sentiment_sum_count],
                key=lambda x: list(calendar.month_name).index(x[0]))

            response = jsonify(
                code=200,
                msg="ok",
                data=monthly_AUS_sentiment_list,
            )
            response.status_code = 200
            return response

        except Exception as e:
            response = jsonify(
                code=500,
                msg="Error occurred: " + str(e),
                data={},
            )
            response.status_code = 500
            return response
