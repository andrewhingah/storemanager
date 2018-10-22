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

		self.users = {'name': 'Barbara Hamisi', 'email': 'hamisi.com', 'password': '1234'}

		self.user = {'name': 'Andrew Hinga', 'email': 'andrewhinga5@gmail.com', 'password': 'password'}

		self.authHeaders = {"Content-Type":"application/json"}
		self.header = {"Content-Type":"application/json"}

		#create a new user
		self.app.post('/api/v1/auth/signup', data=json.dumps(self.user), headers=self.header)

		# login the user
		response = self.app.post("/api/v1/auth/signin", data=json.dumps(self.user), headers=self.header)


if __name__ == '__main__':
	unittest.main()