import twitter_map_clustered
from argparse import ArgumentParser
import unittest
import pytest
import os
import sys
class Test_data(unittest.TestCase):
	def test_verify(self):
		#t = twitter_map_clustered()		
		#t.make_map(t.filename)
		 
		args = 'cluster.html'
		x = self.assertTrue(os.path.exists(args))
		
			
if __name__=='__main__':
	print ("Test case: Check if .html file is created")
	unittest.main()
	
