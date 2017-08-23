# COPYRIGHT (C) MATT PAAUW 2016
# https://github.com/mpaauw/ticker-quote-bot

import praw
from praw.models import MoreComments
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

with open('cache.txt', 'r+') as cache:

    cacheContent = cache.readlines() # load cache content
    cacheContent = [item.strip() for item in cacheContent] # sanitize cache content

    # NOTE: remove submission limit after testing
    # parse all new submissions within default subreddit:
    for submission in reddit.subreddit(sub).new(limit=5): 
        for comment in submission.comments.list():

            # ignore additional comments for now:
            if isinstance(comment, MoreComments):
                continue

            # check cache to see if comment has already been addressed:
            if comment.fullname in cacheContent:
                print('Comment already visited, skipping: [%s]' % (comment.fullname))
                continue

            # check to see if comment contains a body:
            if not hasattr(comment, 'body'):
                continue
            
            # parse comment for summon call:
            if call in comment.body:
                splitBody = comment.body.split('@')
                if len(splitBody) > 1: 
                    ticker = splitBody[1]
                    date = datetime.datetime.now().strftime("%Y-%m-%d")
                    try:
                        data = quandl.Dataset('WIKI/' + ticker).data(params={'start_date':date, 'end_date':date, 'rows':1})
                        comment.reply('[%s] last closing price: [%s]' % (ticker, data[0].close))
                        print('Reply added to Comment: [%s] requesting quote for [%s]' % (comment.fullname, ticker))
                        cache.write(comment.fullname + '\n')
                        print('Comment added to cache: [%s]' % (comment.fullname))                       
                    except:
                        print('Error fetching quote: [%s]\n' % (ticker))
                           