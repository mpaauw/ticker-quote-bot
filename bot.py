# COPYRIGHT (C) MATT PAAUW 2016
# https://github.com/mpaauw/ticker-quote-bot

import praw
import configparser
import quandl
import datetime

config = configparser.ConfigParser()
config.readfp(open("credentials.config"))

clientId = config.get("creds", "clientId")
clientSecret = config.get("creds", "clientSecret")
userAgent = config.get("creds", "userAgent")
username = config.get("creds", "username")
password = config.get("creds", "password")
quandlKey = config.get("creds", "quandlKey")
sub = config.get("creds", "sub")
call = config.get("creds", "call")

quandl.ApiConfig.api_key = quandlKey
reddit = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username)

for submission in reddit.subreddit(sub).new(limit=5):
    for comment in submission.comments.list():
        if not hasattr(comment, 'body'):
            continue
        if call in comment.body:
            splitBody = comment.body.split('@')
            length = len(splitBody)
            if len(splitBody) > 1:
                ticker = splitBody[1]
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                data = quandl.Dataset('WIKI/' + ticker).data(params={'start_date':date, 'end_date':date, 'rows':1})
                comment.reply('[%s] last closing price: [%s]' % (ticker, data[0].close))
        