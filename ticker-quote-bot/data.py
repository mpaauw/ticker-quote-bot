import requests
import json
import sys
from decimal import Decimal
from quote import Quote

class Data:

    key = ''

    def __init__(self, key):
        self.key = key

    def getQuote(self, ticker):
        endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=1min&outputsize=compact&apikey=%s' % (ticker, self.key)
        response = requests.get(endpoint)

        print('[%s]' % (response.status_code))

        try:
            open = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['1. open'])).quantize(Decimal('.01'))
            high = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['2. high'])).quantize(Decimal('.01'))
            low = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['3. low'])).quantize(Decimal('.01'))
            close = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['4. close'])).quantize(Decimal('.01'))
            volume = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (1min)'])).values())[0]['5. volume'])).quantize(Decimal('.01'))

            quote = Quote(open, high, low, close, volume)
            print('%s,%s,%s,%s,%s' % (quote.open, quote.high, quote.low, quote.close, quote.volume))

            return quote
        except Exception as e:
            print(e)      
  