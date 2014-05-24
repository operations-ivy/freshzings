import tweepy, time, sys
from keys import *
#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = list()

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(line)
#    time.sleep(60)#Tweet every minute

#for follower in tweepy.Cursor(api.followers).items():
#    follower.follow()
tweets = api.search(q="zing")
for result in tweets:
        api.update_status(result)

        print tweets
