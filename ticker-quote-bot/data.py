import requests
import json
import sys

class Data:

    key = ''

    def __init__(self, key):
        self.key = key

    def getQuote(self, ticker):
        endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=1min&outputsize=compact&apikey=%s' % (ticker, self.key)
        response = requests.get(endpoint)

        print('[%s]' % (response.status_code))

        try:
            quote = list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['4. close']
            print(quote)
            return quote
        except Exception as e:
            print(e)      
  