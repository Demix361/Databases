from random import choice
from faker import Faker


class Store():
	def __init__(self):
		self.city = None
		self.street = None
		self.house = None
		self.code = None


def get_city_pool(amount):
	fake = Faker("ru-RU")
	pool = []

	for i in range(amount):
		while True:
			a = fake.city()
			if a[0] == 'г' and ',' not in a:
				a = a[3:]

				if a not in pool:
					pool.append(a)
					break

	return pool


def get_address_pool(amount):
	fake = Faker("ru-RU")
	pool = []

	for i in range(amount):
		while True:
			a = fake.street_address()
			j = a.find(',')

			street = (a[:j])
			house = (a[j + 2:])
			postcode = str(fake.postcode())

			if ',' not in street:
				pool.append((street, house, postcode))
				break

	return pool


def to_str(store):
	return store.city + "," + store.street + "," + store.house + "," + store.code + "\n"


def generate_stores(amount, filename):
	address_pool = get_address_pool(1000)
	city_pool = get_city_pool(500)
	stores = []

	for i in range(amount):
		store = Store()
		store.city = choice(city_pool)
		store.street, store.house, store.code = choice(address_pool)
		stores.append(store)

	with open(filename, "w", encoding="utf-8") as f:
		for store in stores:
			f.write(to_str(store))


if __name__ == "__main__":
	generate_stores(1000, "store.csv")
