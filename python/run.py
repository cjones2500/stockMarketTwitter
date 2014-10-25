import tweepy
import dataListener
import sys
import json

##details are specific for a specific account
consumer_key = "gkjJaClVe2dfSKAv6jbVnTGLm"
consumer_secret = "GK5enzXaLSf6l9Upf7o6Bh1dEh53X2hFsmoYqHEx4p7BTg6iIE"
access_token =  "2842922585-jKcjR0YqhOBSxZJ00BdS3GvHjFoizI3d6Ion4II"
access_token_secret = "KGMXdzlMm8ag2sgkl8gh33glw1wQKOtpxTUmQLSGEvWcF"

valueToSearch = sys.argv[1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
result = api.search(valueToSearch)
for i in range(0,10):
    print result[i].text
    print result[i].id
#data = json.loads(results)
#print data
