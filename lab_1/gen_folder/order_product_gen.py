from random import randint


class OrderProduct():
	def __init__(self):
		self.order_id = None
		self.product_id = None
		self.amount = None


def get_amount(filename):
	i = 0

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			i += 1

	return i - 1


def to_line(*args):
	n = len(args)
	res = ""

	for i in range(n):
		res += str(args[i])

		if i == n - 1:
			res += "\n"
		else:
			res += ","

	return res


def generate_order_product(amount, filename, order_db, product_db):
	order_products = []
	order_amount = get_amount(order_db)
	product_amount = get_amount(product_db)
	table_header = "order_id,product_id,amount\n"

	for i in range(amount):
		o = OrderProduct()
		o.order_id = randint(1, order_amount)
		o.product_id = randint(1, product_amount)
		if randint(0, 1) == 0:
			o.amount = 1
		else:
			o.amount = randint(2, 10)

		order_products.append(o)

	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for o in order_products:
			f.write(to_line(o.order_id, o.product_id, o.amount))


if __name__ == "__main__":
	generate_order_product(1000, "order_product.csv", "order.csv", "product.csv")