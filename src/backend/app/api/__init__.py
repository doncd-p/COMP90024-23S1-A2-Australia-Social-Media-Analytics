from flask_restful import Api
from .electorateAllTweets import NumberSentimentAll, DailyAvgSentimentAll, WeeklyAvgSentimentAll, MonthlyAvgSentimentAll
from .electoratePoliticalTweets import NumberSentimentPolitical, DailyAvgSentimentPolitical, WeeklyAvgSentimentPolitical, MonthlyAvgSentimentPolitical
from .tweetsMeta import TweetsMeta
from .tootMeta import TootMeta
from .topTweets import TopPositiveTweets, TopNegativeTweets
<<<<<<< HEAD
from .electorateData import ElectorateGeoData, ElectorateSudoData, ElectorateSudoDataAll
from .boardPolitical import BoardWeeklyAvgSentimentPolitical, BoardDailyAvgSentimentPolitical, BoardMonthlyAvgSentimentPolitical, BoardWinningChangeSentiment
=======
from .electorateData import ElectorateData, ElectorateGeoData
from .boardPolitical import BoardWeeklyAvgSentimentPolitical, BoardDailyAvgSentimentPolitical, BoardMonthlyAvgSentimentPolitical
>>>>>>> ad382b9b (fix: backend update)
from .boardAll import BoardWeeklyAvgSentimentAll, BoardDailyAvgSentimentAll, BoardMonthlyAvgSentimentAll


def init_api(app):
    """
    Initialize the API, adding all routes to the Flask app.

    Args:
        app (Flask): The Flask app
    """

    api = Api()
    api.add_resource(NumberSentimentAll, '/sentiments/number')
    api.add_resource(DailyAvgSentimentAll, '/sentiments/daily')
    api.add_resource(WeeklyAvgSentimentAll, '/sentiments/weekly')
    api.add_resource(MonthlyAvgSentimentAll, '/sentiments/monthly')

    api.add_resource(NumberSentimentPolitical, '/political/sentiments/number')
    api.add_resource(DailyAvgSentimentPolitical, '/political/sentiments/daily')
    api.add_resource(WeeklyAvgSentimentPolitical,
                     '/political/sentiments/weekly')
    api.add_resource(MonthlyAvgSentimentPolitical,
                     '/political/sentiments/monthly')

    api.add_resource(TopPositiveTweets, '/tweet/top_positive')
    api.add_resource(TopNegativeTweets, '/tweet/top_negative')

    api.add_resource(TweetsMeta, '/tweet/meta')
    api.add_resource(TootMeta, '/toot/meta')

    api.add_resource(ElectorateSudoData, '/electorate/sudo_data')
    api.add_resource(ElectorateSudoDataAll, '/electorate/sudo_data/all')
    api.add_resource(ElectorateGeoData, '/electorate/geo_data')

    api.add_resource(BoardWeeklyAvgSentimentAll, '/board/sentiments/weekly')
    api.add_resource(BoardWeeklyAvgSentimentPolitical,
                     '/board/political/sentiments/weekly')
    api.add_resource(BoardDailyAvgSentimentAll,
                     '/board/sentiments/daily')
    api.add_resource(BoardDailyAvgSentimentPolitical,
                     '/board/political/sentiments/daily')
    api.add_resource(BoardMonthlyAvgSentimentAll,
                     '/board/sentiments/monthly')
    api.add_resource(BoardMonthlyAvgSentimentPolitical,
                     '/board/political/sentiments/monthly')
<<<<<<< HEAD
    api.add_resource(BoardWinningChangeSentiment,
                     '/board/political/sentiments/winningchange')
=======
>>>>>>> ad382b9b (fix: backend update)

    api.init_app(app)
