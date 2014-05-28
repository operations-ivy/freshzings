import tweepy, time, sys
from keys import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

results = api.search(q="zing", count=2)

for i in results:
    api.update_status(i)
    time.sleep(7200) # Tweet every 2 hours