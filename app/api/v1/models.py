from datetime import datetime

class Products:
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

class Sales:
	sales = {}
	sale_id = 1

	def __init__(self, name, quantity, category, price):
		self.sale_id = len(Sales.sales) + 1
		self.name = name
		self.quantity = quantity
		self.category = category
		self.total_price = price * self.quantity
		self.date_sold = datetime.now()

	def save(self):
		payload = dict(
			item_id = self.sale_id,
			name = self.name,
			quantity = self.quantity,
			category = self.category,
			total_price = self.total_price)

		self.sales.update({self.sale_id:payload})

	def get_all(self):
		return Sales.sales

	def get_one(self, sale_id):
		for key in Sales.sales:
			if key == sale_id:
				return Sales.sales[key]
		message = "Sale record not found"
		return message

# class User:
# 	def __init__(self,email,password):
# 		self.email = email
# 		self.password = password

# class Attendant(User):
# 	def __init__()