"""
Products testing module
"""
import json
from .base_test import BaseTestCase

class TestSales(BaseTestCase):
	"""
	class for testing products endpoints
	"""

	def test_get(self):
		"""Test user can get all sales
		"""
		response = self.app.get('/api/v1/sales')
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 200)
		self.assertEqual(result["message"], "success")

	def test_post(self):
		"""test create a sale record
		"""
		response = self.app.post('/api/v1/sales',
			data=json.dumps(self.sales_data),
			headers=self.authHeaders)
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 201)
		self.assertEqual(result["message"], "success")
		self.assertEqual(result["status"], "created")

	def test_get_one_sale_record(self):
		"""test get a specific sale_record by id
		"""
		response = self.app.post('/api/v1/sales',
			data=json.dumps(self.sales_data),
			headers=self.authHeaders)
		result = json.loads(response.data.decode())

		self.assertEqual(response.status_code, 201)

		res = self.app.get('/api/v1/sale/{}'.format(
			result["sale_record"]["sale_id"]))	
		self.assertEqual(res.status_code, 200)

	def test_get_non_existing_product(self):
		"""test a non existing sale_record cannot be retrieved
		"""
		response = self.app.get('/api/v1/sale/100')
		self.assertEqual(response.status_code, 404)

		result = json.loads(response.data.decode())
		self.assertEqual(result["message"], "sale record unavailable")
		self.assertEqual(result["status"], "not found")