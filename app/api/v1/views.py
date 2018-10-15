from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

products = []

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('quantity')
parser.add_argument('price')

class Products(Resource):
	"""All products class"""
	def get(self):
		"""gets all products"""
		return {"Products":products}

	def post(self):
		"""posts a single product"""
		pass