import tweepy

consumer_key = "jkSBxdXkiPapU2lJL3w9NIrtt" 
consumer_secret = "RfetsUtgpjVU5bRSinY3ll5ojc9pqq9OAA33wZxsyuTa5N83KQ" 

access_token = "1007971559389179904-PUKQ3cXJOMFwmIQrK9SQofQxEIPziC"
access_token_secret = "df0P5I9Y37l4YZIOGdIScbX5GILoNc7dYaeqdB7b94EVQ" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
follow = api.followers()

for follows in follow:
	with open('followers.txt', 'a') as file:
		file.write("@" + follows.screen_name + "\n")



#	 follows.screen_name