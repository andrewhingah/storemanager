from flask import Flask, Blueprint
from flask_restful import Resource, Api

from instance.config import app_config

from .api.v1.views.products_views import AllProducts, SingleProduct
from .api.v1.views.sales_views import AllSales, SingleSale

version1 = Blueprint('api', __name__)
api = Api(version1)

def create_app(config_name):
	app=Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	app.register_blueprint(version1, url_prefix='/api/v1')
	api.add_resource(AllProducts, '/products')
	api.add_resource(SingleProduct, '/product/<int:product_id>')
	api.add_resource(AllSales, '/sales')
	api.add_resource(SingleSale, '/sale/<int:sale_id>')

	return app