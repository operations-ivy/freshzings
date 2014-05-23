import tweepy, time, sys
from keys import *
#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(line)
#    time.sleep(60)#Tweet every minute

#for follower in tweepy.Cursor(api.followers).items():
#    follower.follow()


new = api.create_saved_search('http://search.twitter.com/search.json?q=%23zing')

search = [api.saved_searches(new)]
s=search.readlines()
search.close()

for line in s:
        api.update_status(line)
        time.sleep(60)