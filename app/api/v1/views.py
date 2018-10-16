from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

products = {}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="quantity cannot be blank")
parser.add_argument('price', type=int, required=True, help="price cannot be blank")

class Products(Resource):
	"""All products class"""
	def get(self):
		"""gets all products"""
		return {"Products":products}

	def post(self):
		"""posts a single product"""
