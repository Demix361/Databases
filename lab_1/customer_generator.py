from random import randint, choice
from faker import Faker
from stock_generator import get_store_id_pool, get_index_pool


class Customer():
	def __init__(self):
		self.name = "None"
		self.phone = "None"
		self.index = "None"
		self.store_id = "None"
		self.date = "None"


def get_name_faker():
	fake = Faker()
	return fake.name()


def get_name(pool):
	return choice(pool)


def get_name_pool():
	fake = Faker()
	pool = []

	for i in range(1000):
		pool.append(fake.name())

	return pool


def get_phone():
	phone = "+79"

	for i in range(9):
		phone += str(randint(0, 9))

	return phone


def get_index(pool):
	return choice(pool)


def get_store_id(pool):
	return choice(pool)


def get_date_faker():
	fake = Faker()
	raw = fake.date().split("-")

	return str(raw[2]) + "." + str(raw[1]) + "." + str(raw[0])


def get_date():
	month_max = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	month = randint(1, 12)
	day = randint(1, month_max[month - 1])
	year = str(randint(2010, 2019))
	if month < 10:
		month = "0" + str(month)
	else:
		month = str(month)
	if day < 10:
		day = "0" + str(day)
	else:
		day = str(day)

	return day + "." + month + "." + year


def to_str(c):
	return c.name + "," + c.phone + "," + c.index + "," + c.store_id + "," + c.date + "\n"


def generate_customers(amount, filename, item_db, store_db):
	customers = []
	index_pool = get_index_pool(item_db)
	store_id_pool = get_store_id_pool(store_db)
	name_pool = get_name_pool()

	for i in range(amount):
		customer = Customer()
		customer.name = get_name(name_pool)
		customer.phone = get_phone()
		customer.index = get_index(index_pool)
		customer.store_id = get_store_id(store_id_pool)
		customer.date = get_date()

		customers.append(customer)

	with open(filename, "w") as f:
		for c in customers:
			f.write(to_str(c))


if __name__ == "__main__":
	generate_customers(1000, "customers.txt", "items.txt", "stores.txt")
