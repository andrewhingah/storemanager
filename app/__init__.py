from flask import Flask, Blueprint

from flask_jwt_extended import JWTManager

from instance.config import app_config
from .api.v1.views.home import home

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	jwt = JWTManager(app)

	from .api.v1 import version1 as v1

	app.register_blueprint(home)

	app.register_blueprint(v1)

	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	return app


