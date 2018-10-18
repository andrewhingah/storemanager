import unittest
import json

from ... import create_app

class BaseTestCase(unittest.TestCase):
	'''Base tests class'''
	def setUp(self):
		"""
		tests setup
		"""
		self.app = create_app('testing').test_client()
		self.products_data = {"name":"unga", "quantity":22, "price":100}
		self.sales_data = {"name":"laptop", "quantity":33, "category": "electronics", "price":55000}
		self.authHeaders = {"Content-Type":"application/json"}

if __name__ == '__main__':
	unittest.main()