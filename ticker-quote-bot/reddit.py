import praw
from praw.models import MoreComments
import datetime
import sys

class Reddit:

    instance = None
    call = ''

    def __init__(self, clientId, clientSecret, password, userAgent, username, call):
        self.instance = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username) 
        self.call = call

    def parseSubmissions(self, sub, data):
        with open('ticker-quote-bot\cache.txt', 'r+') as cache:
            
            cacheContent = cache.readlines()
            cacheContent = [item.strip() for item in cacheContent]  

            for submission in self.instance.subreddit(sub).new():
                for comment in submission.comments.list():

                    if isinstance(comment, MoreComments):
                        continue

                    if comment.fullname in cacheContent:
                        print('Comment already visited, skipping: [%s]' % (comment.fullname))
                        continue

                    if not hasattr(comment, 'body'):
                        continue
                    
                    if self.call in comment.body:
                        splitBody = comment.body.split('@')
                        if len(splitBody) > 1: 
                            ticker = splitBody[1]
                            date = datetime.datetime.now().strftime("%Y-%m-%d")
                            try:
                                quote = data.getQuote(ticker)
                                comment.reply('[%s] last closing price: [%s]' % (ticker, quote))
                                print('Reply added to Comment: [%s] requesting quote for [%s]' % (comment.fullname, ticker))
                                cache.write(comment.fullname + '\n')
                                print('Comment added to cache: [%s]' % (comment.fullname))
                            except Exception as e:
                                print('Error fetching quote: [%s]' % (ticker))
                                print(e)
