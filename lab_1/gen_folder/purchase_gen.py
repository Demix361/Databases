from random import randint, choice


class Purchase():
	def __init__(self):
		self.client_id = None
		self.product_id = None
		self.store_id = None
		self.amount = None
		self.datetime = None


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


def get_amount(filename):
	i = 0

	with open(filename, "r") as f:
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


def get_datetime(beg, end):
	# 1999-01-08 04:05:06
	year = str(randint(beg, end))
	month = str(randint(1, 12))
	if len(month) == 1:
		month = "0" + month
	day = str(randint(1, 28))
	if len(day) == 1:
		day = "0" + day

	hour = str(randint(0, 23))
	if len(hour) == 1:
		hour = "0" + hour
	minute = str(randint(0, 59))
	if len(minute) == 1:
		minute = "0" + minute
	sec = str(randint(0, 59))
	if len(sec) == 1:
		sec = "0" + sec

	datetime = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + sec

	return datetime


def generate_purchase(amount, filename, client_db, product_db, store_db):
	purchases = []
	client_amount = get_amount(client_db)
	product_pool = get_product_pool(product_db)
	store_amount = get_amount(store_db)
	table_header = "client_id,product_id,store_id,amount,purchase_time\n"

	for i in range(amount):
		p = Purchase()
		p.client_id = randint(1, client_amount)
		p.product_id = choice(product_pool)
		p.store_id = randint(1, store_amount)
		p.amount = randint(1, 3)
		p.purchase_time = get_datetime(2016, 2019)

		purchases.append(p)

	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for p in purchases:
			f.write(to_line(p.client_id, p.product_id, p.store_id, p.amount, p.purchase_time))


if __name__ == "__main__":
	generate_purchase(1000, "purchase.csv", "client.csv", "product.csv", "store.csv")

