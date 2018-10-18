"""
Products testing module
"""
import json
from .base_test import BaseTestCase


class TestProducts(BaseTestCase):
	"""
	class for testing products endpoints
	"""

	def test_get(self):
		"""Test admin/attendant can get all products
		"""
		response = self.app.get('/api/v1/products')
		self.assertEqual(response.status_code, 200)

	def test_post(self):
		"""test post a product
		"""
		response = self.app.post('/api/v1/products',
			data=json.dumps(self.products_data),
			headers=self.authHeaders)
		self.assertEqual(response.status_code, 201)

	def test_get_one_product(self):
		"""test get a specific product by id
		"""
		response = self.app.post('/api/v1/products',
			data=json.dumps(self.products_data),
			headers=self.authHeaders)
		self.assertEqual(response.status_code, 201)

		res = self.app.get('/api/v1/product/1')	
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_product(self):
		"""test a non existing product cannot be retrieved
		"""
		response = self.app.get('/api/v1/product/100')
		self.assertEqual(response.status_code, 404)