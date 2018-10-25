''
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from ..models.sales_model import Sales
from .. models.products_model import *


parser = reqparse.RequestParser()
parser.add_argument('product_id', required=True, help="Id cannot be blank")
# parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")
# parser.add_argument('category', required=True, help="Category cannot be blank")
# parser.add_argument('price', type=int, required=True, help="only integers allowed")

class AllSales(Resource):
	"""All products class"""
	
	@jwt_required
	def get(self):
		"""gets all products"""
		sales = Sales.get_all(self)
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"sales":sales}),
		200)


	@jwt_required
	def post(self):
		"""posts a single product"""
		args = parser.parse_args()
		product_id = args['product_id']
		quantity = args['quantity']
	
		for k,v in Products.products.items():
			if k == int(product_id):
				remaining_q = Products.products[k]["quantity"] - quantity
				name = Products.products[k]["name"]
				category = Products.products[k]["category"]
				price = Products.products[k]["price"]
				if remaining_q <= 0:
					return {"message":"The quantity you want to sell exceeds the available inventory"}
				new_sale = Sales(product_id, name, quantity, remaining_q, category, price)
				Products.products[int(product_id)]["quantity"] = remaining_q

				new_sale.save()
				return make_response(jsonify(
					{"message":"success",
					"status":"created",
					"sale_record":new_sale.__dict__}), 201)
		
		return make_response(jsonify({"message":"Product unavailable"}))

class SingleSale(Resource):
	'''Single sale record API'''
	@jwt_required
	def get(self, sale_id):
		one_sale = Sales.get_one(self, sale_id)

		if one_sale == "Sale record not found":
			return make_response(jsonify(
				{"status":"not found",
				"message":"sale record unavailable",
				}), 404)
			
		return make_response(jsonify(
			{"status":"ok",
			"message":"success",
			"product":one_sale}
			), 200)