from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from .models import Sales

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")
parser.add_argument('category', required=True, help="Category cannot be blank")
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
		category = args['category']
		price = args['price']

		new_sale = Sales(name, quantity, category, price)
		new_sale.save()

		return make_response(jsonify(
			{"message":"success",
			"status":"created",
			"sale_record":new_sale.__dict__}
			), 201)
