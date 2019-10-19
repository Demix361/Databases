from random import randint, choice, shuffle


class Stock():
	def __init__(self):
		self.store_id = None
		self.product_id = None
		self.quantity = None


def get_store_amount(filename):
	i = 0

	with open(filename, "r") as f:
		for line in f:
			i += 1

	return i - 1


def get_product_pool(filename):
	pool = []
	i = 0

	with open(filename, "r") as f:
		for line in f:
			if i != 0:
				product_id = line[:line.find(",")]

				pool.append(product_id)
			else:
				i += 1

	return pool


def to_str(stock):
	return str(stock.store_id) + "," + stock.product_id + "," + str(stock.quantity) + "\n"


def generate_stock(filename, product_db, store_db):
	stock_list = []
	product_pool = get_product_pool(product_db)
	store_amount = get_store_amount(store_db)
	table_header = "store_id,product_id,quantity\n"

	for i in range(store_amount):
		for j in range(len(product_pool)):
			stock = Stock()
			stock.store_id = i + 1
			stock.product_id = product_pool[j]
			stock.quantity = randint(0, 500)
			stock_list.append(stock)

	with open(filename, "w") as f:
		f.write(table_header)
		for s in stock_list:
			f.write(to_str(s))


if __name__ == "__main__":
	generate_stock("stock.csv", "product.csv", "store.csv")
