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
	def setUp(self):
		"""
		create a testing client
		"""
		self.app = create_app('testing').test_client()
		# self.app =create_app.test_client()
		self.content_type = 'application/json'

	def test_get(self):
		"""Test admin/attendant can get all products
		"""
		response = self.app.get('/api/v1/products')
		self.assertEqual(response.status_code, 200)

	def test_post(self):
		product = {"name":"unga","price":100}
		response = self.app.post('/api/v1/products', data=json.dumps(product))
		self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
	unittest.__main__