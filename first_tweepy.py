import tweepy

consumer_key  
consumer_secret   

access_token 
access_token_secret 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
follow = api.followers()

for follows in follow:
	with open('followers.txt', 'a') as file:
		file.write("@" + follows.screen_name + "\n")



#	 follows.screen_name
