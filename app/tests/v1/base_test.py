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
        self.new_user = {'email': 'john@gmail.com', 'username':'john', 'password': '1881'} 
    
        self.client = self.app.test_client()

        self.products_data = {"name":"unga", "quantity":22, "price":100}
        self.sales_data = {"name":"laptop", "quantity":33, "category": "electronics", "price":55000}


        self.user = {'email': 'henry@gmail.com','username': 'henry','password': 'password'}

        self.header = {"Content-Type": "application/json"}

        self.s_url = 'api/v1/auth/signup' #signup url
        self.l_url = 'api/v1/auth/login' #login url
        self.p_url = 'api/v1/products' #products url
        self.sl_url = 'api/v1/sales' #sales url
        

    def register_user(self, email='', username='', password=''):

    	user_data = self.users

    	return self.checker.post(self.s_url, data=user_data)

    def login_user(self, email='', password=''):
    	
    	user_data =self.users

    	response = self.checker.post(self.l_url, data=user_data)
    	return response


if __name__ == "__main__":
	unittest.main()
