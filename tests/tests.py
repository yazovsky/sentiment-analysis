import unittest
import twitter
import sentiment
import json

class TwitterTest(unittest.TestCase):
    def test(self):
        res = twitter.search('python')
        print(res)
        self.assertGreater(len(res), 1)

class PredictorTest(unittest.TestCase):
    def test(self):
        s = "Dear Alex,\n\nMahalo. The movie is awesome. I didn't ruin it. \n\nEnjoy,\n\nD to the J https://t.co/rDyir8hgzi"
        prediction = sentiment.predict(s)
        print(prediction)
        self.assertGreater(prediction['pos'], prediction['neg'])
