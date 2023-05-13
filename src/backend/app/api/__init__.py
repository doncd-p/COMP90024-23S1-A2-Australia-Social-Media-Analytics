from flask_restful import Api
from .electorateAllTweets import DateSentimentAll, DateAvgSentimentAll, WeeklyAvgSentimentAll
from .electoratePoliticalTweets import DateSentimentPolitical, DateAvgSentimentPolitical, WeeklyAvgSentimentPolitical
from .tweetsMeta import TweetsMeta
from .tootMeta import TootMeta
from .topTweets import TopPositiveTweets, TopNegativeTweets


def init_api(app):
    """
    Initialize the API, adding all routes to the Flask app.

    Args:
        app (Flask): The Flask app
    """

    api = Api()
    api.add_resource(DateSentimentAll, '/sentiments/daterange')
    api.add_resource(DateAvgSentimentAll, '/sentiments/avg/daterange')
    api.add_resource(WeeklyAvgSentimentAll, '/sentiments/avg/weekly')

    api.add_resource(DateSentimentPolitical, '/political/sentiments/daterange')
    api.add_resource(DateAvgSentimentPolitical,
                     '/political/sentiments/avg/daterange')
    api.add_resource(WeeklyAvgSentimentPolitical,
                     '/political/sentiments/avg/weekly')

    api.add_resource(TopPositiveTweets, '/tweet/top_positive')
    api.add_resource(TopNegativeTweets, '/tweet/top_negative')

    api.add_resource(TweetsMeta, '/tweet/meta')
    api.add_resource(TootMeta, '/toot/meta')

    api.init_app(app)
