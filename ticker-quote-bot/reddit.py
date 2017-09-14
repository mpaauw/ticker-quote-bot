import praw
from praw.models import MoreComments
import sys

class Reddit:

    searchUrl = 'https://www.google.com/search?q=stock+quote+'
    instance = None
    call = None
    metrics = None
    logger = None

    def __init__(self, clientId, clientSecret, password, userAgent, username, call, metrics, logger):
        self.instance = praw.Reddit(client_id=clientId, client_secret=clientSecret, password=password, user_agent=userAgent,  username=username) 
        self.call = call
        self.metrics = metrics
        self.logger = logger
        self.logger.write('Reddit instantiated.')

    def parseUnreadItems(self, data):
        unreadItems = self.instance.inbox.unread()
        for item in unreadItems:
            if not hasattr(item, 'body'):
                self.logger.write('Item [%s] has no body content, skipping.' % (item.fullname))
                continue
            if self.call in item.body:
                splitBody = item.body.split('@')
                if len(splitBody) > 1: 
                    ticker = splitBody[1]
                    self.logger.write('Ticker: [%s] requested by Item: [%s]' % (ticker, item.fullname))
                    try:
                        quote = data.getQuote(ticker)
                        reply = self.buildReply(ticker, quote)
                        item.reply(reply)
                        print('Reply added to Comment: [%s] requesting quote for [%s]' % (item.fullname, ticker))
                        self.logger.write('Reply added to Item [%s] requesting quote for [%s]' % (item.fullname, ticker))
                        item.mark_read()
                        self.logger.write('Item [%s] marked as read' % (item.fullname))
                        self.metrics.trackItem(True)
                    except Exception as e:
                        self.logger.write('Error fetching Quote [%s] for Item [%s]' % (ticker, item.fullname))
                        self.logger.writeError(e)
                        print('Error fetching quote: [%s]' % (ticker))
                        print(e)
            else:
                item.mark_read()
                self.logger.write('Item [%s] marked as read' % (item.fullname))
                self.metrics.trackItem(False)

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
                                commentReply = self.buildReply(ticker, quote)
                                comment.reply(commentReply)
                                print('Reply added to Comment: [%s] requesting quote for [%s]' % (comment.fullname, ticker))
                                cache.write(comment.fullname + '\n')
                                print('Comment added to cache: [%s]' % (comment.fullname))
                            except Exception as e:
                                print('Error fetching quote: [%s]' % (ticker))
                                print('Error: [' + e + ']')
                    self.metrics.trackComment()
                self.metrics.trackSubmission()

    def buildReply(self, ticker, quote):
        upperTicker = ticker.upper()
        searchLink = '[%s](%s%s)' % (upperTicker, self.searchUrl, upperTicker)
        comment = 'Ticker|Open|High|Low|Close|Volume\n:-|:-|:-|:-|:-|:-\n%s|%s|%s|%s|%s|%s\n' % (searchLink, quote.open, quote.high, quote.low, quote.close, quote.volume)
        return comment
