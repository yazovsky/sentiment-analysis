import logging

# Debug mode allows you to get much more information about process, but it could be too much information for production.
# Thus, logging level should be 'DEBUG' for debug and development purpose, but 'INFO' for production running.
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")

TWITTER_CONSUMER_KEY = "SOME"
TWITTER_CONSUMER_SECRET = "SOME"
TWITTER_ACCESS_TOKEN = "SOME"
TWITTER_ACCESS_TOKEN_SECRET = "SOME"

PORT = 8099
