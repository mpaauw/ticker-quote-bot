# COPYRIGHT (C) MATT PAAUW 2016
# https://github.com/mpaauw/ticker-quote-bot

import praw
from praw.models import MoreComments
import configparser
import quandl
import datetime

# load config data:
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

quandl.ApiConfig.api_key = quandlKey # load quandl instance
reddit = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username) # load reddit instance via praw

with open('cache.txt', 'r+') as cache: # open cache while processing new posts
    cacheContent = cache.readlines() # load cache content
    cacheContent = [item.strip() for item in cacheContent] # sanitize cache content
   
    for submission in reddit.subreddit(sub).new(): # parse all new submissions within default subreddit (no limit):
        for comment in submission.comments.list():

            # ignore additional comments for now:
            if isinstance(comment, MoreComments):
                continue

            # check cache to see if comment has already been addressed:
            if comment.fullname in cacheContent:
                print('Comment already visited, skipping: [%s]' % (comment.fullname)) ##
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
                    try: # attempt to retrieve and reply quote data specified within summon:
                        data = quandl.Dataset('WIKI/' + ticker).data(params={'start_date':date, 'end_date':date, 'rows':1})
                        comment.reply('[%s] last closing price: [%s]' % (ticker, data[0].close)) # post reply to summoner 
                        print('Reply added to Comment: [%s] requesting quote for [%s]' % (comment.fullname, ticker)) ##
                        cache.write(comment.fullname + '\n') # now that summoner's comment has been addressed, cache it to avoid in the future
                        print('Comment added to cache: [%s]' % (comment.fullname)) ##              
                    except: # data was not fetched and / or read properly
                        print('Error fetching quote: [%s]' % (ticker)) ##
