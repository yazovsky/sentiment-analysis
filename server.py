import web
import logging
import json
import time

import twitter as twitterClient

import sentiment
import settings

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")
urls = (
    '/train(.*)', 'train',
    '/predict(.*)', 'predict',
    '/twitter(.*)', 'twitter',
    '/email(.*)', 'email'
)

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

app = MyApplication(urls, globals())

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

class email:

    # submit a Twitter username for analysis
    def GET(self, name):
        logging.debug(web.data())
        render = web.template.render('templates/')
        return render.index("")

    # submit a Twitter username for analysis
    def POST(self, name):
        logging.debug(web.data())

        text = web.input(text="").text
        prediction_result = sentiment.predict(text)

        render = web.template.render('templates/')
        return render.index(prediction_result)

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

class twitter:

    # get results summary of sentiment analysis for given Twitter username
    def GET(self, name):
        logging.debug(web.data())
        search = web.input(search="").search
        logging.debug('sentence: '+search)
        start_time = current_milli_time()

        result = {}
        twitter_search = twitterClient.search(search)
        for idx, twit in enumerate(twitter_search):
            result[str(idx)] = {
                'text': twit,
                'rate': sentiment.predict(twit)
            }

        res = {
            'status': 'ok',
            'took': current_milli_time() - start_time,
            'result': result
        }
        web.header('Content-Type', 'application/json')
        return json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__":
    app.run(port=settings.PORT)
