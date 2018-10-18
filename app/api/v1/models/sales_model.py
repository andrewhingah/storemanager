from datetime import datetime

class Sales:
	'''Class represents sales operations'''
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
