import tweepy

##details are specific for a specific account
consumer_key = "gkjJaClVe2dfSKAv6jbVnTGLm"
consumer_secret = "GK5enzXaLSf6l9Upf7o6Bh1dEh53X2hFsmoYqHEx4p7BTg6iIE"
access_token =  "2842922585-jKcjR0YqhOBSxZJ00BdS3GvHjFoizI3d6Ion4II"
access_token_secret = "KGMXdzlMm8ag2sgkl8gh33glw1wQKOtpxTUmQLSGEvWcF"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class listener(tweepy.StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track=["car"])

#You can fetch the rate limit status
print api.rate_limit_status()
##returns a series of values within a json format

##public_tweets = api.home_timeline()
##for tweet in public_tweets:
##    print tweet.text
##    print "\n"
##print api.me()

