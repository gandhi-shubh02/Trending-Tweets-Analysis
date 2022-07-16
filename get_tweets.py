import json
from tweepy import Cursor
from twitter_client import twitter_client 

class get_tweets():
	def __init__(self):
		self.filename='home_timeline.jsonl'
		

	def get_data(self, filename):
		c=twitter_client()
		client = c.get_twitter_client()
		#twitter_client.get_twitter_client(self)
		with open(filename, 'w') as f:
			for page in Cursor(client.home_timeline, count=200, include_rts=True).pages(4):
				for status in page:
					# Process a single status
					f.write(json.dumps(status._json)+"\n")
	
