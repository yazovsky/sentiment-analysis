# What is this
Simple sentiment analysis service. For any given text it would return sentiment analysis result in a format of neutral, negative, positive rates. For example

```
{
  "compound": -0.296,
  "neg": 0.095,
  "neu": 0.905,
  "pos": 0.0
}
```

where 'compound' is overal result.

# Public playground

Twitter: Analyze sentiment of popular tweets using search keyword. E.g. "US Election 2016": <http://52.44.14.137:8999/twitter?search=election>

Simple web form where you can submit random data: <http://52.44.14.137:8999/email>

# Run locally

## Option 1: with Docker

pre-requirements: packages Docker and Git installed, port 8099 available

```
git clone git@github.com:softrin/sentiment-analysis.git
cd sentiment-analysis
docker build -t sentiments-analysis .
docker run -r -P 8099:8099 sentiments-analysis
```

## Option 2: with Python

pre-requirements: packages installed Python >=2.7 and pip, port 8099 available

```
git clone git@github.com:softrin/sentiment-analysis.git
cd sentiment-analysis
pip install -r requirements.txt
python server.py
```

Don't forget to train the model (it is not by default), by running <http://localhost:8099/train>

# Usage

Twitter: Analyze sentiment of popular tweets using search keyword. E.g. "US Election 2016": <http://localhost:8099/twitter?search=election>

Simple web form where you can submit random data: <http://localhost:8099/email>
