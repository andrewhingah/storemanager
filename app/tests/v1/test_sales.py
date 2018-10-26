"""
Sales testing module
"""
import json
from .base_test import BaseTestCase

class TestSales(BaseTestCase):
	"""
	class for testing sales endpoints
	"""

	def test_get_all_sales(self):
		"""Test user can get all sales
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.get(self.sl_url,
			headers=dict(Authorization="Bearer " + access_token))
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["message"], "success")

	def test_get_sales_without_authentication(self):
		'''test products cannot be accessed before login'''
		response = self.client.get(self.sl_url)
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 401)
		self.assertEqual(result["msg"], "Missing Authorization Header")


	def test_post_sale_record(self):
		"""test create a sale record
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		res = self.client.post(self.p_url,
			data=self.products_data,
			headers=dict(Authorization="Bearer " + access_token))
		result = json.loads(res.data.decode())
		self.assertEqual(res.status_code, 201)
		self.assertEqual(result["message"], "success")
		self.assertEqual(result["status"], "created")

		# response = self.client.post(self.sl_url,
		# 	data=self.sales_data,
		# 	headers=dict(Authorization="Bearer " + access_token))
		# result = json.loads(response.data.decode())

		# self.assertEqual(response.status_code, 201)
		# self.assertEqual(result["message"], "success")
		# self.assertEqual(result["status"], "created")


	def test_get_one_sale_record(self):
		"""test get a specific sale_record by id
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.post('/api/v1/sales',
			data=self.sales_data,
			headers=dict(Authorization="Bearer " + access_token))
		
		self.assertEqual(response.status_code, 200)

		# res = self.client.get('/api/v1/sale/1',
		# 	headers=dict(Authorization="Bearer " + access_token))	
		# self.assertEqual(res.status_code, 200)

	def test_get_non_existing_sale_record(self):
		"""test a non existing sale_record cannot be retrieved
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		response = self.client.get('/api/v1/sale/100',
			headers=dict(Authorization="Bearer " + access_token))
		self.assertEqual(response.status_code, 404)

		result = json.loads(response.data.decode())
		self.assertEqual(result["message"], "sale record unavailable")
		self.assertEqual(result["status"], "not found")

	def test_post_sale_record_with_quantity_string(self):
		"""test create a sale record with quantity as string
		"""
		self.register_user()
		result = self.login_user()
		access_token = json.loads(result.data.decode())['token']

		res = self.client.post(self.sl_url,
			data=self.string_sales,
			headers=dict(Authorization="Bearer " + access_token))
		result = json.loads(res.data.decode())
		self.assertEqual(res.status_code, 400)
		self.assertEqual(result["message"]["quantity"], "Only integers allowed")