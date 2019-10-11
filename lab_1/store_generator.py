from random import randint, choice


class Store():
	def __init__(self):
		self.id = None
		self.city = None


def get_id(pool):
	abc = "qwertyuiopasdfghjklzxcvbnm"
	while True:
		index = choice(abc) + str(randint(1000, 9999))

		if index not in pool:
			pool.append(index)
			return index


def get_city():
	city_pool = ["Moscow", "St. Petersburg", "Novosibirsk", "Yekaterinburg",
	"Nizhny Novgorod", "Kazan", "Samara", "Omsk", "Chelyabinsk",
	"Rostov-on-Don", "Ufa"]

	return choice(city_pool)


def to_str(store):
	return store.id + "," + store.city + "\n"


def generate_stores(amount, filename):
	id_pool = []
	stores = []

	for i in range(amount):
		store = Store()
		store.id = get_id(id_pool)
		store.city = get_city()

		stores.append(store)

	with open(filename, "w") as f:
		for store in stores:
			f.write(to_str(store))


if __name__ == "__main__":
	generate_stores(1000, "stores.txt")

