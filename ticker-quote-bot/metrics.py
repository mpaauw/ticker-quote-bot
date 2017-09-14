import time

class Metrics:

    startTime = None
    endTime = None
    totalTime = None
    totalReadItems = 0
    totalRepliedItems = 0
    avgReadTime = 0
    avgReplyTime = 0
    totalComments = 0
    totalSubmissions = 0
    avgCommentTime = 0
    avgSubmissionTime = 0
    logger = None

    def __init__(self, logger):
        self.logger = logger
        self.logger.write('Metrics instantiated.')

    def buildInboxReport(self):
        print('\n')
        print('================================')
        print('--- TICKER-QUOTE-BOT METRICS ---')
        print('--------- Inbox Report ---------')
        print('================================')
        print('Total Items Read:            [%s]' % (self.totalReadItems))
        print('Total Items Replied:         [%s]' % (self.totalRepliedItems))
        print('Avg Time / Read:             [%s seconds (rough)]' % (self.avgReadTime))
        print('Avg Time / Reply:            [%s seconds (rough)]' % (self.avgReplyTime))
        print('Total Running Time:          [%s seconds]' % (self.totalTime))
        print('================================')
        print('\n')

        self.logger.write('================================')
        self.logger.write('--- TICKER-QUOTE-BOT METRICS ---')
        self.logger.write('--------- Inbox Report ---------')
        self.logger.write('================================')
        self.logger.write('Total Items Read:            [%s]' % (self.totalReadItems))
        self.logger.write('Total Items Replied:         [%s]' % (self.totalRepliedItems))
        self.logger.write('Avg Time / Read:             [%s seconds (rough)]' % (self.avgReadTime))
        self.logger.write('Avg Time / Reply:            [%s seconds (rough)]' % (self.avgReplyTime))
        self.logger.write('Total Running Time:          [%s seconds]' % (self.totalTime))
        self.logger.write('================================')

    def buildSubmissionsReport(self):
        print('\n')
        print('================================')
        print('--- TICKER-QUOTE-BOT METRICS ---')
        print('------ Submission  Report ------')
        print('================================')
        print('Total Comments Parsed:       [%s]' % (self.totalComments))
        print('Total Submissions Parsed:    [%s]' % (self.totalSubmissions))
        print('Avg Time / Comment:          [%s seconds (rough)]' % (self.avgCommentTime))
        print('Avg Time / Submission:       [%s seconds (rough)]' % (self.avgSubmissionTime))
        print('Total Running Time:          [%s seconds]' % (self.totalTime))
        print('================================')
        print('\n')

        self.logger.write('================================')
        self.logger.write('--- TICKER-QUOTE-BOT METRICS ---')
        self.logger.write('------ Submission  Report ------')
        self.logger.write('================================')
        self.logger.write('Total Comments Parsed:       [%s]' % (self.totalComments))
        self.logger.write('Total Submissions Parsed:    [%s]' % (self.totalSubmissions))
        self.logger.write('Avg Time / Comment:          [%s seconds (rough)]' % (self.avgCommentTime))
        self.logger.write('Avg Time / Submission:       [%s seconds (rough)]' % (self.avgSubmissionTime))
        self.logger.write('Total Running Time:          [%s seconds]' % (self.totalTime))
        self.logger.write('================================')

    def start(self):
        self.startTime = self.getTime()
        self.logger.write('Time started.')   
    
    def end(self):
        self.endTime = self.getTime()
        self.totalTime = self.endTime - self.startTime
        if self.totalReadItems > 0:
            self.avgReadTime = self.totalTime / self.totalReadItems
        if self.totalRepliedItems > 0:
            self.avgReplyTime = self.totalTime / self.totalRepliedItems
        if self.totalComments > 0:
            self.avgCommentTime = self.totalTime / self.totalComments
        if self.totalSubmissions > 0: 
            self.avgSubmissionTime = self.totalTime / self.totalSubmissions
        self.logger.write('Time ended.')

    def getTime(self):
        self.logger.write('Time captured.')
        return time.clock()

    def trackItem(self, replied):
        if(replied):
            self.totalRepliedItems += 1
            self.totalReadItems += 1
            self.logger.write('Reply tracked.')
        else:
            self.totalReadItems += 1
            self.logger.write('Read item tracked.')

    def trackComment(self):
        self.totalComments += 1
        self.logger.write('Comment tracked.')
    
    def trackSubmission(self):
        self.totalSubmissions += 1
        self.logger.write('Submission tracked.')
