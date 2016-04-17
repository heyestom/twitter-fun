import sys
from  twitter import *

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN =  'xxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
ts = TwitterStream(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

hodor_stream = ts.statuses.filter(track="Hodor")

replies_index = 0
replies = ["Hodor?","Hodor!","Hodor.","Hodor! Hodor!", "Hodor! Hodor?", "Hodor Hodor?","Hodor! Hodor Hodor?", "Hodor Hodor!", "Hodor", "Hodor, Hodor Hodor.", "Hodor Hodor! Hodor.","Hodor! Hodor! Hodor"]

for tweet in hodor_stream:
	#don't do retweets
	if 'retweeted_status' not in tweet and 'RT' not in tweet['text']:
		# don't tweet at yourself or these other accounts!
		if tweet['user']['screen_name'] != "hodorclock" and tweet['user']['screen_name'] != "I___Hodor___I" and tweet['user']['screen_name'] != "FidelFoolek" and tweet['user']['screen_name'] != "____hodor____":
			print '\nincomming: ' + tweet['user']['screen_name'], tweet['text']
			status = '@' + tweet['user']['screen_name'] + ' ' + replies[replies_index]
			print '\noutgoing reply: ' + status
			t.statuses.update(status=status, in_reply_to_status_id=tweet['id'])

			replies_index += 1
			if replies_index >= len(replies):
				sys.exit(0)
