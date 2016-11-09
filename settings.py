import logging

# Debug mode allows you to get much more information about process, but it could be too much information for production.
# Thus, logging level should be 'DEBUG' for debug and development purpose, but 'INFO' for production running.
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")

TWITTER_CONSUMER_KEY = "47eElZrxEf9kKXWVVqs8SN1KC"
TWITTER_CONSUMER_SECRET = "3x03fhlOQA9ntM8qeDXPDCO2MoMcHyqDvDfzdH7FYbgXcm3um9"
TWITTER_ACCESS_TOKEN = "17496707-iP1zq2mWxltSdJ8UiCxwBEiFpybpRhuAxNjSEyFMu"
TWITTER_ACCESS_TOKEN_SECRET = "GSvbGyN2KJ7T8cAKyq70WIvLcjNVglJFOhHulSFf2HqjK"

PORT = 8099