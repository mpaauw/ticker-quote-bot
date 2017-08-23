import quandl

class Data:

    def __init__(self, key):
        quandl.ApiConfig.api_key = key # load quandl instance

    def getQuote(ticker, date):
        return quandl.Dataset('WIKI/' + ticker).data(params={'start_date':date, 'end_date':date, 'rows':1})