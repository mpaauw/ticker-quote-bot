import requests
import json
import sys
from decimal import Decimal
from quote import Quote

class Data:

    key = None
    logger = None

    def __init__(self, key, logger):
        self.key = key
        self.logger = logger
        self.logger.write('Data instantiated.')

    def getQuote(self, ticker):
        endpoint = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=%s' % (ticker, self.key)
        response = requests.get(endpoint)
        print('Status Code: [%s]' % (response.status_code))
        try:
            open = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (Daily)'])).values())[0]['1. open'])).quantize(Decimal('.01'))
            high = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (Daily)'])).values())[0]['2. high'])).quantize(Decimal('.01'))
            low = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (Daily)'])).values())[0]['3. low'])).quantize(Decimal('.01'))
            close = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (Daily)'])).values())[0]['4. close'])).quantize(Decimal('.01'))
            volume = Decimal(str(list(json.loads(json.dumps(response.json()['Time Series (Daily)'])).values())[0]['5. volume'])).quantize(Decimal('.01'))
            quote = Quote(open, high, low, close, volume)
            print('%s,%s,%s,%s,%s' % (quote.open, quote.high, quote.low, quote.close, quote.volume))
            self.logger.write('Quote successfully retrieved (status code: [%s]) for ticker [%s]' % (response.status_code, ticker))
            return quote
        except Exception as e:
            self.logger.writeError(e)
            print(e)      
  