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

    def start(self):
        self.startTime = self.getTime()     
    
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

    def getTime(self):
        return time.clock()

    def trackItem(self, replied):
        if(replied):
            self.totalRepliedItems += 1
            self.totalReadItems += 1
        else:
            self.totalReadItems += 1

    def trackComment(self):
        self.totalComments += 1
    
    def trackSubmission(self):
        self.totalSubmissions += 1
