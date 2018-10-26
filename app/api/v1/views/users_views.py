from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
import re

from ..models.users_model import User
from ..utils.validate import validate_email, verify_user_details


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('username')
parser.add_argument('password')

class UserRegistration(Resource):
	"""All products class"""

	def post(self):
		"""Register a new user"""
		
		args = parser.parse_args()
		email = args['email']
		username = args['username']
		password = args['password']

		if verify_user_details(username):
			return verify_user_details(username)
		if validate_email(email):
			return validate_email(email)

		new_user = User.get_one(self, email)

		if new_user == "User not found":
			new_user = User(email, username, password)
			new_user.signup()

			return make_response(jsonify(
				{"message":"User created!",
				"user":new_user.__dict__}
				), 201)
		else:
			return make_response(jsonify({'message':'Email already exists.'}))

class UserLogin(Resource):
	'''user login class'''
	def post(self):
		args = parser.parse_args()
		email = args['email']
		password = args['password']

		user = User.get_one(self, email)

		if user == "User not found":
			return make_response(jsonify(
				{
				"message":"Your account does not exist!, Please Register!",
				}), 401)
		else:
			token = create_access_token(identity=email)
			return make_response(jsonify({'message': 'Logged in successfully!', 'token': token}), 201)