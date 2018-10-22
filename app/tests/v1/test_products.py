"""
Products testing module
"""
import json
from .base_test import BaseTestCase


class TestProducts(BaseTestCase):
	"""
	class for testing products endpoints
	"""

	def test_get_all_products(self):
		"""Test admin/attendant can get all products
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']
		response = self.client.get(self.p_url,
			headers=dict(Authorization="Bearer " + access_token))
		self.assertEqual(response.status_code, 200)

	def test_post_product(self):
		"""test post a product
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post(self.p_url,
			headers=dict(Authorization="Bearer " + access_token),
			data=self.products_data)
		self.assertEqual(response.status_code, 201)

	def test_post_product_with_no_name(self):
		'''test post product request must have a name'''
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post(self.p_url,
			headers=dict(Authorization="Bearer " + access_token),
			data=self.bad_products_data1)
		result = json.loads(response.data.decode())
		self.assertEqual(response.status_code, 400)
		self.assertEqual(result["message"]["name"], "Name cannot be blank")

	def test_quantity_cannot_be_a_string(self):
		'''test only integers allowed in quantity'''
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post(self.p_url,
			headers=dict(Authorization="Bearer " + access_token),
			data=self.bad_products_data2)
		self.assertEqual(response.status_code, 400)



	def test_get_one_product(self):
		"""test get a specific product by id
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post(self.p_url,
			data=self.products_data,
			headers=dict(Authorization="Bearer " + access_token))
		self.assertEqual(response.status_code, 201)

		res = self.client.get('/api/v1/product/1',
			headers=dict(Authorization="Bearer " + access_token))	
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_product(self):
		"""test a non existing product cannot be retrieved
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.get('/api/v1/product/100',
			headers=dict(Authorization="Bearer " + access_token))
		self.assertEqual(response.status_code, 404)