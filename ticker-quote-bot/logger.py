import logging

class Logger:

    def __init__(self, location):
        logging.basicConfig(filename=location, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.debug('\n\n')
    
    def write(self, message):
        logging.debug(message)
    
    def writeError(self, errorMessage):
        logging.error(errorMessage)