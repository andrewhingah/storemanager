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
        
        self.client = self.app.test_client()

        self.users = {'email': 'andrewhinga5@gmail.com', 'username': 'andrew5', 'password': '1234'}
        self.new_user = {'email': 'john@gmail.com', 'username':'john', 'password': '1881'}
        self.bad_user = {'email': 'henry@gmail.com','username':"henry5"}


        self.header = {"Content-Type": "application/json"}

        self.s_url = 'api/v2/auth/signup' #signup url
        self.l_url = 'api/v2/auth/login' #login url
        self.p_url = 'api/v2/products' #products url
        self.sl_url = 'api/v2/sales' #sales url

        with self.app.app_context():
            #initialize database



if __name__ == "__main__":
    unittest.main()
