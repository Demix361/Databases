from random import randint, choice, shuffle


class Stock():
	def __init__(self):
		self.store_id = None
		self.index = None
		self.amount = None


def get_store_id_pool(filename):
	pool = []

	with open(filename, "r") as f:
		for line in f:
			store_id = line[:line.find(",")]
			if store_id not in pool:
				pool.append(store_id)

	return pool


def get_index_pool(filename):
	pool = []

	with open(filename, "r") as f:
		for line in f:
			index = line[:line.find(",")]
			if index not in pool:
				pool.append(index)

	return pool


def get_amount():
	return randint(30, 1500)


def to_str(stock):
	return stock.store_id + "," + stock.index + "," + str(stock.amount) + "\n"


def generate_stock(filename, item_db, store_db):
	stock_list = []
	index_pool = get_index_pool(item_db)
	store_id_pool = get_store_id_pool(store_db)

	for i in range(len(store_id_pool)):
		shuffle(index_pool)

		for j in range(randint(0, len(index_pool))):
			stock = Stock()
			stock.store_id = store_id_pool[i]
			stock.index = index_pool[j]
			stock.amount = get_amount()
			stock_list.append(stock)

	with open(filename, "w") as f:
		for s in stock_list:
			f.write(to_str(s))


if __name__ == "__main__":
	generate_stock("stock.txt", "items.txt", "stores.txt")
