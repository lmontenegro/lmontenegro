class Cart:

	def __init__(self, request):
		self.request = request
		self.session = request.session
		cart = self.session.get("cart")
		if not cart:
			self.session["cart"] = {}
			self.cart = self.session["cart"]
		else:
			self.cart = cart

	def add(self,item):
		id = str(item.id)
		if id not in self.cart.keys():
			self.cart[id] = {
				"item_id": item.id,
				"name": item.name,
				"accumulated": int(item.price),
				"cantity": 1,
			}
		else:
			self.cart[id]["cantity"] += 1
			self.cart[id]["accumulated"] += int(item.price)
		self.saveCart()

	def saveCart(self):
		self.session["cart"] = self.cart
		self.modified = True

	def delete(self, item):
		id = str(item.id)
		if id in self.cart:
			del self.cart[id]
			self.save()

	def deduct(self, item):
		id = str(item.id)
		if id in self.cart.keys():
			self.cart[id]["cantity"] -= 1
			self.cart[id]["accumulated"] -= item.price
			if self.cart[id]["cantity"] <= 0:
				self.delete(item)
			self.save()

	def clean(self):
		self.session["cart"] = {}
		self.session.modified = True