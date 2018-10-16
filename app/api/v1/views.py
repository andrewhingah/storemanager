from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

products = {}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="quantity cannot be blank")
parser.add_argument('price', type=int, required=True, help="price cannot be blank")

class AllProducts(Resource):
	"""All products class"""
	def get(self):
		"""gets all products"""
		return {"Products":products}

	def post(self):
		"""posts a single product"""
		id = len(products) + 1
		args = parser.parse_args()

		payload = {
		'name':args['name'],
		'quantity':args['quantity'],
		'price':args['price']
		}

		products[id] = payload

		return make_response(jsonify({"message":"success",
			"status":"created",
			"sale":payload}), 201)

class SingleProduct(Resource):
	'''single product API'''
	def get(self, id):
		for key in products:
			if key == id:
				return products[id]
		message = "Product not found"
		return {"message":message}
