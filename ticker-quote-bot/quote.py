class Quote:
    open = 0.0
    high = 0.0
    low = 0.0
    close = 0.0
    volume = 0.0

    def __init__(self, open, high, low, close, volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume