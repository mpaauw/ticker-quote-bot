import configparser

class Configuration:

    clientId = ''
    clientSecret = ''
    userAgent = ''
    username = ''
    password = ''
    quandlKey = ''
    sub = ''
    call = ''

    def __init__(self):
        config = configparser.ConfigParser()
        config.readfp(open("ticker-quote-bot\credentials.config"))
        self.clientId = config.get("creds", "clientId")
        self.clientSecret = config.get("creds", "clientSecret")
        self.userAgent = config.get("creds", "userAgent")
        self.username = config.get("creds", "username")
        self.password = config.get("creds", "password")
        self.quandlKey = config.get("creds", "quandlKey")
        self.sub = config.get("creds", "sub")
        self.call = config.get("creds", "call")        
