from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from .models import Sales

app = Flask(__name__)
api = Api(app)

# products = {}

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")
parser.add_argument('price', type=int, required=True, help="only integers allowed")

class AllSales(Resource):
	"""All products class"""
	def get(self):
		"""gets all products"""
		sales = Sales.get_all(self)
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"sales":sales}),
		200)

	def post(self):
		"""posts a single product"""
		
		args = parser.parse_args()
		name = args['name']
		quantity = args['quantity']
		price = args['price']

		new_sale = Sales(name, quantity, price)
		new_sale.save()

		return make_response(jsonify(
			{"message":"success",
			"status":"created",
			"product":newproduct.__dict__}
			), 201)

class SingleProduct(Resource):
	'''single product API'''
	def get(self, product_id):
		one_product = Products.get_one(self, product_id)

		if one_product == "Product not found":
			return make_response(jsonify(
				{"status":"not found",
				"message":"product unavailbale",
				}), 404)
			
		return make_response(jsonify(
			{"status":"ok",
			"message":"success",
			"product":one_product}
			), 200)
			
