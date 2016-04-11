from  twitter import *

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN =  'xxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
ts = TwitterStream(auth=OAuth(CONSUMER_KEY, CONSUMER_SECRET,OAUTH_TOKEN, OAUTH_SECRET))

groot_stream = ts.statuses.filter(track='Groot')

for tweet in groot_stream:
	tweet_id = tweet['id']
	print 'incomming: ' + tweet['user']['screen_name'], tweet['text']
	status = '@' + tweet['user']['screen_name'] + ' ' + 'I am Groot!'
	print 'outgoing reply: ' + status
	t.statuses.update(status=status, in_reply_to_status_id=tweet_id)
