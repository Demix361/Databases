from random import randint, choice, random
from faker import Faker
from stock_generator import get_store_id_pool, get_index_pool


class Customer():
	def __init__(self):
		self.id = None
		self.name = None
		self.phone = None
		self.city = None
		self.status = None


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


def get_phone_pool(amount):
	pool = []

	for i in range(amount):
		while True:
			num = get_phone()
			if num not in pool:
				pool.append(num)
				break

	return pool


def get_city_pool():
	cities = ["Moscow", "St. Petersburg", "Novosibirsk", "Yekaterinburg",
	"Nizhny Novgorod", "Kazan", "Samara", "Omsk", "Chelyabinsk",
	"Rostov-on-Don", "Ufa"]

	return cities


def get_status():
	sts = [("bronze", 45), ("silver", 30), ("gold", 18), ("diamond", 12)]

	num = random() * 100
	s = 0

	for i in range(len(sts)):
		s += sts[i][1]

		if num < s:
			return sts[i][0]

	return None


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


def generate_customers(amount, filename):
	customers = []
	name_pool = get_name_pool()
	phone_pool = get_phone_pool(amount)
	city_pool = get_city_pool()

	for i in range(amount):
		customer = Customer()
		customer.id = i + 1
		customer.name = choice(name_pool)
		customer.phone = phone_pool[i]
		customer.city = choice(city_pool)
		customer.status = get_status()

		customers.append(customer)

	with open(filename, "w") as f:
		for c in customers:
			f.write(to_line(c.id, c.name, c.phone, c.city, c.status))


if __name__ == "__main__":
	generate_customers(1000, "customers.txt")
