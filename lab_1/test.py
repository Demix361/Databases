from faker import Faker

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

def f():
	return (1, 2, 3)

a, b, c = f()
print(a, b)

