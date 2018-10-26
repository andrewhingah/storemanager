from flask_restful import Api
from flask import Blueprint

from .views.products_views import AllProducts, SingleProduct
from .views.sales_views import AllSales, SingleSale
from .views.users_views import UserRegistration, UserLogin

version1 = Blueprint('api version1', __name__, url_prefix='/api/v1')

api = Api(version1)


api.add_resource(AllProducts, '/products')
api.add_resource(SingleProduct, '/product/<int:product_id>')
api.add_resource(AllSales, '/sales')
api.add_resource(SingleSale, '/sale/<int:sale_id>')
api.add_resource(UserRegistration, '/auth/signup')
api.add_resource(UserLogin, '/auth/login')