from flask import Flask, Blueprint
from flask_restful import Resource, Api

from instance.config import app_config

from .api.v1.views import AllProducts, SingleProduct

version1 = Blueprint('api', __name__)
api = Api(version1)

def create_app(config_name):
	app=Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	app.register_blueprint(version1, url_prefix='/api/v1')
	api.add_resource(AllProducts, '/products')
	api.add_resource(SingleProduct, '/product/<int:id>')

	return app