"""
Products testing module
"""
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
		self.app = create_app('testing')
		self.app =create_app.test_client()

	def test_get(self):
		"""Test admin/attendant can get all products
		"""
		response = self.app.get('/products')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.__main__