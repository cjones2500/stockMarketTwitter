import tweepy
from tweepy import StreamListener

class dataListener(StreamListener):
    def __init__(self):
        self.on_data = self.onDataReturned
        self.on_error = self.onErrorReturned

    def onDataReturned(self,data):
        print "Data returned"
        print data
        return True
    
    def onErrorReturned(self,error):
        print "Error returned..."
        print error
