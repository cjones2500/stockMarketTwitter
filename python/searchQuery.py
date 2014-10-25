import tweepy,json
from tweepy import API    

class Crawler(API):
    #initialise the api with itself and details
    def __init__(self,auth):
        self.auth = auth
        self.api = API(self.auth)
    
    def search(self,query):
        print "Searching for '" + query + "'\n"
        self.data =  self.api.search(query)
        return self.data

consumer_key = "gkjJaClVe2dfSKAv6jbVnTGLm"
consumer_secret = "GK5enzXaLSf6l9Upf7o6Bh1dEh53X2hFsmoYqHEx4p7BTg6iIE"
access_token =  "2842922585-jKcjR0YqhOBSxZJ00BdS3GvHjFoizI3d6Ion4II"
access_token_secret = "KGMXdzlMm8ag2sgkl8gh33glw1wQKOtpxTUmQLSGEvWcF"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

crawler = Crawler(auth)
print crawler.search("hello")
