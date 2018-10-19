from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.users_model import User


parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="email cannot be blank")
parser.add_argument('username')
parser.add_argument('password', required=True, help="password cannot be blank")

class UserRegistration(Resource):
	"""All products class"""

	def post(self):
		"""Register a new user"""
		
		args = parser.parse_args()
		email = args['email']
		username = args['username']
		password = args['password']

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
				"message":"User not found",
				}), 404)
		else:
			token = create_access_token(identity=args['email'])
			return make_response(jsonify({'message': 'Logged in successfully!', 'token': token}), 201)
		return make_response('Your account does not exist!, Please Register!'), 401