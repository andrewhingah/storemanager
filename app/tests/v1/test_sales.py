"""
Products testing module
"""
import json
import unittest


from ... import create_app


class TestProducts(unittest.TestCase):
	"""
	class for testing products endpoints
	"""

	data = {"name":"laptop", "quantity":33, "category": "electronics", "price":55000}

	def setUp(self):
		"""
		create a testing client
		"""
		self.app = create_app('testing').test_client()

	def test_get(self):
		"""Test user can get all sales
		"""
		response = self.app.get('/api/v1/sales')
		self.assertEqual(response.status_code, 200)
	def test_post(self):
		"""test create a sale record
		"""
		response = self.app.post('/api/v1/sales',
			data=json.dumps(self.data),
			content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_get_one_sale_record(self):
		"""test get a specific sale_record by id
		"""
		response = self.app.post('/api/v1/sales',
			data=json.dumps(self.data),
			content_type='application/json')
		self.assertEqual(response.status_code, 201)

		res = self.app.get('/api/v1/sale/1')	
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_product(self):
		"""test a non existing sale_record cannot be retrieved
		"""
		response = self.app.get('/api/v1/sale/100')
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.__main__