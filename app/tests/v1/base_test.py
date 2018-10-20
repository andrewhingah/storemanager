'''Base test class that defines
setup and initializes data'''

import unittest
import json

from ... import create_app

class BaseTestCase(unittest.TestCase):
    """Parent tests class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        
        self.checker = self.app.test_client()
        self.users = {'email': 'andrewhinga5@gmail.com', 'username': 'andrew5', 'password': '1234'}
        self.default_user = {'email': 'john@gmail.com', 'username':'john', 'password': '1881'} 
    
        self.client = self.app.test_client()
        self.products_data = {"name":"unga", "quantity":22, "price":100}
        self.sales_data = {"name":"laptop", "quantity":33, "category": "electronics", "price":55000}


        self.user = {'email': 'andrewhinga5@gmail.com', 'username': 'andrew5','password': 'password'}
        self.header = {"Content-Type": "application/json"}
        

    def register_user(self, email='andrewhinga5@gmail.com', username='andrew', password='1234'):
    	user_data = {
    	'email':email,
    	'username':username,
    	'password':password
    	}

    	return self.checker.post('api/v1/auth/signup', data=user_data)

    def login_user(self, email='andrewhinga5@gmail.com', password='1234'):
    	user_data = {
    	'email':email,
    	'password':password
    	}

    	response = self.checker.post('api/v1/auth/login', data=user_data)
    	return response


if __name__ == "__main__":
	unittest.main()
