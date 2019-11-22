from random import randint, choice
from datetime_gen import get_datetime


class Order():
	def __init__(self):
		self.client_id = None
		self.store_id = None
		self.cashier_id = None
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

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			i += 1

	return i - 1


def get_cashier_pool(filename):
	job_id = [1, 2]
	i = 0
	pool = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			if i != 0:
				if int(line.split(",")[-1]) in job_id:
					pool.append(i)
			i += 1

	return pool



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



def generate_order(amount, filename, client_db, store_db, employee_db):
	orders = []
	client_amount = get_amount(client_db)
	store_amount = get_amount(store_db)
	cashier_pool = get_cashier_pool(employee_db)
	table_header = "client_id,store_id,cashier_id,order_time\n"

	for i in range(amount):
		o = Order()
		o.client_id = randint(1, client_amount)
		o.store_id = randint(1, store_amount)
		o.cashier_id = choice(cashier_pool)
		o.order_time = get_datetime("2013-01-01", "2019-12-31")

		orders.append(o)

	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for o in orders:
			f.write(to_line(o.client_id, o.store_id, o.cashier_id, o.order_time))


if __name__ == "__main__":
	generate_order(1000, "order.csv", "client.csv", "store.csv", "employee.csv")

