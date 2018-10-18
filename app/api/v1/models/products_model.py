from datetime import datetime

class Products:
	'''Class represents operations related to products'''
	products = {}
	
	product_id = 1

	def __init__(self, name, quantity, price):
		self.product_id =len(Products.products) + 1
		self.name = name
		self.quantity = quantity
		self.price = price
		self.date_created = datetime.now()


	def save(self):
		payload = dict(
			product_id = self.product_id,
			name = self.name,
			quantity = self.quantity,
			price = self.price
			)

		self.products.update({self.product_id:payload})

	def get_all(self):
		return Products.products

	def get_one(self, product_id):

		for key in Products.products:
			if key == product_id:
				return Products.products[key]
		message = "Product not found"
		return message