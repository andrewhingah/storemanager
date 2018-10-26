'''Tests for users'''
import json
from .base_test import BaseTestCase


class UsersTestCase(BaseTestCase): 
    """This class represents Users tests."""

        
    def test_signup_user_with_existing_email(self):
        """Test to register user with existing email."""
        data = self.users
        response = self.checker.post(self.s_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'],'Email already exists.')

    def test_signup_new_user(self):
        """Test to register new user."""
        data = self.new_user
        response = self.checker.post(self.s_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'],'User created!')


    def test_signin_user(self):
        """Test user sign in to their account."""
        data = self.users
        response = self.checker.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Logged in successfully!")

    def test_signin_user_with_incorrect_password(self):
        """Test user sign in to their account."""
        data = self.incorrect_pass
        response = self.checker.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "password Incorrect")



    def test_signin_non_registered_user(self):
        """Test signing in a non-registered user."""
        data = self.new_user
        response = self.checker.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Your account does not exist!, Please Register!")

    def test_signup_user_with_missing_fields(self):
        '''test user cannot be signed up with missing fields'''
        data = self.bad_user
        response = self.checker.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message']['email'], "email cannot be blank")

    def test_signup_with_invalid_email(self):
        '''test valid email'''
        data = self.invalid_email
        response = self.checker.post(self.l_url, data=json.dumps(data), headers=self.header)
        result = json.loads(response.data.decode())
        self.assertIn('is not a valid email address', result['message'])


    def test_signup_new_user_with_empty_strings(self):
        """Test signup user with empty strings."""
        data = self.empty_str
        response = self.checker.post(self.s_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'],'This cannot be empty')
        self.assertEqual(response.status_code, 400)


