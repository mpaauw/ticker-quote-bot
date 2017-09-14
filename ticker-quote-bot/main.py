from config import Configuration
from reddit import Reddit
from data import Data
from metrics import Metrics
from logger import Logger

configuration = Configuration()
loggerInstance = Logger(configuration.logLocation)

metrics = Metrics(loggerInstance)
metrics.start()

r = Reddit(configuration.clientId, configuration.clientSecret, configuration.password, configuration.userAgent, configuration.username, configuration.call, metrics)
data = Data(configuration.apiKey)

r.parseUnreadItems(data)

metrics.end()
metrics.buildInboxReport()
