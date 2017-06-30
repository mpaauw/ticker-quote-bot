# COPYRIGHT (C) MATT PAAUW 2016
# https://github.com/mpaauw/ticker-quote-bot

import praw
import configparser

config = configparser.ConfigParser()
config.readfp(open("credentials.config"))

clientId = config.get("creds", "clientId")
clientSecret = config.get("creds", "clientSecret")
userAgent = config.get("creds", "userAgent")
username = config.get("creds", "username")
password = config.get("creds", "password")

reddit = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username)

reddit.subreddit('test').submit('Test Post Please Ignore, Fam', url='https://reddit.com')
