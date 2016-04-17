import sys
from twitter import *

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN =  'xxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
ts = TwitterStream(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

replies_index = 0
replies = [	"I am Groot?","I am Groot!","I am Groot.",
			"I AM GROOT!", "I am Groot??",
			"I am Groot!!!", "I am Groot" ]

# find any tweets which containt the word Groot
groot_stream = ts.statuses.filter(track='Groot')

for index, tweet in enumerate(groot_stream):
  	#don't do retweets
	if 'retweeted_status' not in tweet and "RT" not in tweet['text']:
		# don't tweet at yourself!
		if tweet['user']['screen_name'] != "___iamgroot___":
			print "\nincomming: " + tweet['user']['screen_name'], tweet['text']
			status = "@" + tweet['user']['screen_name'] + " " + replies[replies_index]
			print "\noutgoing reply: " + status
			t.statuses.update(status=status, in_reply_to_status_id=tweet['id'])

			replies_index += 1
			if replies_index >= len(replies):
				sys.exit(0)
