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

	data = {"name":"unga", "quantity":22, "price":100}

	def setUp(self):
		"""
		create a testing client
		"""
		self.app = create_app('testing').test_client()

	def test_get(self):
		"""Test admin/attendant can get all products
		"""
		response = self.app.get('/api/v1/products')
		self.assertEqual(response.status_code, 200)

	def test_post(self):
		"""test post a product
		"""
		# product = {"name":"unga", "quantity":22, "price":100}
		response = self.app.post('/api/v1/products',
			data=json.dumps(self.data),
			content_type='application/json')
		self.assertEqual(response.status_code, 201)

	def test_get_one_product(self):
		"""test get a specific product by id
		"""
		response = self.app.post('/api/v1/products',
			data=json.dumps(self.data),
			content_type='application/json')
		self.assertEqual(response.status_code, 201)

		res = self.app.get('/api/v1/product/1')	
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_product(self):
		"""test a non existing product cannot be retrieved
		"""
		response = self.app.get('/api/v1/product/100')
		self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
	unittest.__main__