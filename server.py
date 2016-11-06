import web
import logging
import json
import time

import sentiment

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")
urls = (
    '/train/(.*)', 'train',
    '/predict/(.*)', 'predict'
)
app = web.application(urls, globals())

current_milli_time = lambda: int(round(time.time() * 1000))

class train:

    # submit a Twitter username for analysis
    def GET(self, name):
        logging.debug(web.data())
        start_time = current_milli_time()

        # re-train model
        sentiment.train()

        res = {
            'status': 'ok',
            'took': current_milli_time() - start_time
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

class predict:

    # get results summary of sentiment analysis for given Twitter username
    def GET(self, name):
        logging.debug(web.data())
        sentence = web.input(sentence="").sentence
        logging.debug('sentence: '+sentence)
        start_time = current_milli_time()

        result = sentiment.predict(sentence)
        
        res = {
            'status': 'ok',
            'took': current_milli_time() - start_time,
            'result': str(result)
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

if __name__ == "__main__":
    app.run()
