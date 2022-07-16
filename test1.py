#from  twitter_client import*
#from twitter_client import get_twitter_client

from twitter_client import twitter_client
import unittest 
import pytest


class Test_client_auth(unittest.TestCase):
	#@staticmethod	
	def testverify(self):
		t = twitter_client()
		print ("hello")
		self.assertEqual(t.consumer_key, "fJriwU9JcNHkzAJYJ7PoI7ftH")
		
		
if __name__=='__main__':
	
	unittest.main()
	
	
	
	
	
