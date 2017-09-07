import time

class Metrics:

    startTime = None
    endTime = None
    totalTime = None
    totalComments = 0
    totalSubmissions = 0
    avgCommentTime = None
    avgSubmissionTime = None
    
    def buildReport(self):
        print('\n')
        print('================================')
        print('--- TICKER-QUOTE-BOT METRICS ---')
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
        self.avgCommentTime = self.totalTime / self.totalComments
        self.avgSubmissionTime = self.totalTime / self.totalSubmissions

    def getTime(self):
        return time.clock()

    def trackComment(self):
        self.totalComments += 1
    
    def trackSubmission(self):
        self.totalSubmissions += 1
