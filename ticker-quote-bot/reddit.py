import praw
from praw.models import MoreComments
import sys

class Reddit:

    searchUrl = 'https://www.google.com/search?q=stock+quote+'
    instance = None
    call = ''
    metrics = None

    def __init__(self, clientId, clientSecret, password, userAgent, username, call, metrics):
        self.instance = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username) 
        self.call = call
        self.metrics = metrics

    def parseSubmissions(self, sub, data):
        with open('ticker-quote-bot\cache.txt', 'r+') as cache:

            cacheContent = cache.readlines()
            cacheContent = [item.strip() for item in cacheContent]  

            for submission in self.instance.subreddit(sub).new():
                flattenedComments = submission.comments.list()

                for comment in flattenedComments:

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
                            try:
                                quote = data.getQuote(ticker)
                                commentReply = self.buildCommentReply(ticker, quote)
                                comment.reply(commentReply)
                                print('Reply added to Comment: [%s] requesting quote for [%s]' % (comment.fullname, ticker))
                                cache.write(comment.fullname + '\n')
                                print('Comment added to cache: [%s]' % (comment.fullname))
                            except Exception as e:
                                print('Error fetching quote: [%s]' % (ticker))
                                print(e)

                    self.metrics.trackComment()

                self.metrics.trackSubmission()

    def buildCommentReply(self, ticker, quote):
        upperTicker = ticker.upper()
        searchLink = '[%s](%s%s)' % (upperTicker, self.searchUrl, upperTicker)
        comment = 'Ticker|Open|High|Low|Close|Volume\n:-|:-|:-|:-|:-|:-\n%s|%s|%s|%s|%s|%s\n' % (searchLink, quote.open, quote.high, quote.low, quote.close, quote.volume)
        return comment
