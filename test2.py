from get_tweets import get_tweets
import unittest
import pytest
import os
import sys
class Test_data(unittest.TestCase):
	def test_verify(self):
		t = get_tweets()		
		t.get_data(t.filename)
		self.assertTrue(os.path.exists(t.filename))
if __name__=='__main__':
	unittest.main()
