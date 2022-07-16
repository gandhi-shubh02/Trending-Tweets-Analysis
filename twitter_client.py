import os
import sys
from tweepy import API
from tweepy import OAuthHandler
class twitter_client():
	def __init__(self):
		try:
			self.consumer_key = "fJriwU9JcNHkzAJYJ7PoI7ftH"
			self.consumer_secret="0h7hGZitUT3l4p6WawTVoPdPE9NNyvfhGixi7EBVPh1pjwfQ7c"
			self.access_token ="1084095074-K4hbfrQZpEGbtacf8y1FZmflrHc7RkZtssdUnZt"
			self.access_secret ="hXy7OuQhg855PQqsHo0TpeotFvntzkpNs89BB6KpmgsV8"
		except  KeyError:
			sys.stderr.write("TWITTER_* environment variables not set\n")
			sys.exit(1)    

	def get_twitter_auth(self):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)
		return auth

	def get_twitter_client(self):
		auth = self.get_twitter_auth()
		client = API(auth)
		return client

		
