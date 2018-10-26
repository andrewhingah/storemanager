from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from flask_jwt import JWT, jwt_required
from flask_jwt_extended import jwt_required

from ..models.products_model import Products


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")
parser.add_argument('category')
parser.add_argument('price')

class AllProducts(Resource):
	"""All products class"""
	@jwt_required
	def get(self):
		"""gets all products"""
		products = Products.get_all(self)
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"products":products}),
		200)

	@jwt_required
	def post(self):
		"""posts a single product"""
		
		args = parser.parse_args()
		name = args['name']
		quantity = args['quantity']
		category = args['category']
		price = args['price']

		newproduct = Products(name, quantity, category, price)
		newproduct.save()

		return make_response(jsonify(
			{"message":"success",
			"status":"created",
			"product":newproduct.__dict__}
			), 201)

class SingleProduct(Resource):
	'''single product API'''
	@jwt_required
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
