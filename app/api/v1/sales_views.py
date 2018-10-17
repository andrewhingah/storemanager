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
