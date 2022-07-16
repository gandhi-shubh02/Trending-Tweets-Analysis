import twitter_make_geojson 
from argparse import ArgumentParser
import unittest
import pytest
import os
import sys
class Test_data(unittest.TestCase):
	def print_test(self):
			print ("Test case: Check if .geo.json file is created")
			
	def test_verify(self):
		#t = twitter_make_geojson()
		#t.make_geojson(t.filename)
		self.print_test()
		args = 'timeline.geo.json'
		x = self.assertTrue(os.path.exists(args))


if __name__=='__main__':
	print ("Test case: Check if .geo.json file is created")
	unittest.main()
	
	
