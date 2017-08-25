from config import Configuration
from reddit import Reddit
from data import Data

configuration = Configuration()
r = Reddit(configuration.clientId, configuration.clientSecret, configuration.password, configuration.userAgent, configuration.username, configuration.call)
data = Data(configuration.apiKey)

r.parseSubmissions(configuration.sub, data)
