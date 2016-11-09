import settings
import json
from twython import Twython

def search(query):
    twitter = Twython(app_key = settings.TWITTER_CONSUMER_KEY,
                      app_secret=settings.TWITTER_CONSUMER_SECRET,
                      oauth_token=settings.TWITTER_ACCESS_TOKEN,
                      oauth_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
    result = twitter.search(q=query, result_type='popular', count=100)
    return [elem['text'] for elem in result['statuses']]