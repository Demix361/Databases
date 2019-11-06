from random import randint, choice


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


def get_product_pool(filename):
	pool = []
	i = 0

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			if i != 0:
				product_id = line[:line.find(",")]

				pool.append(product_id)
			else:
				i += 1

	return pool


def generate_order_product(filename, order_db, product_db):
	order_products = []
	order_amount = get_amount(order_db)
	product_pool = get_product_pool(product_db)
	table_header = "order_id,product_id,amount\n"

	for i in range(order_amount):
		used_products = []
		position_amount = randint(1, 8)
		for j in range(position_amount):
			o = OrderProduct()

			o.order_id = i + 1

			while True:
				product = choice(product_pool)

				if product not in used_products:
					used_products.append(product)
					o.product_id = product
					break

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
	generate_order_product("order_product.csv", "order.csv", "product.csv")