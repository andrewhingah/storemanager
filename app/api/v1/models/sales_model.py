from datetime import datetime

class Sales:
	'''Class represents sales operations'''
	sales = {}
	
	sale_id = 1

	def __init__(self, product_id, name, quantity, remaining_q, category, price):
		self.sale_id = len(Sales.sales) + 1
		self.product_id = product_id
		self.name = name
		self.quantity = quantity
		self.category = category
		self.remaining_q = remaining_q
		self.total_price = int(price) * self.quantity
		self.date_sold = datetime.now()

	def save(self):
		payload = dict(
			sale_id = self.sale_id,
			name = self.name,
			quantity = self.quantity,
			remaining_q = self.remaining_q,
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
