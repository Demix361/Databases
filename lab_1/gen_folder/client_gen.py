from random import randint, choice, random
from faker import Faker


class Client():
	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.sex = None
		self.phone = None
		self.email = None
		self.status = None


def get_name_pool(amount):
	fake = Faker("ru-RU")
	female = []
	male = []

	for i in range(amount):
		fio = fake.name().split()
		if len(fio) != 3:
			fio = fio[1:]
		
		if fio[2][-1] == "а":
			female.append(fio[:2])
		elif fio[2][-1] == "ч":
			male.append(fio[:2])

	return male, female


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


def get_email_pool(amount):
	pool = []
	fake = Faker()

	for i in range(amount):
		email = fake.email()
		pool.append(email)

	return pool


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


def generate_clients(amount, filename):
	clients = []
	male, female = get_name_pool(amount)
	phone_pool = get_phone_pool(amount)
	email_pool = get_email_pool(amount)
	table_header = "first_name,last_name,sex,phone,email,status\n"

	for i in range(amount):
		client = Client()
		if randint(0, 1) == 0:
			client.last_name, client.first_name = choice(male)
			client.sex = "male"
		else:
			client.last_name, client.first_name = choice(female)
			client.sex = "female"
		client.phone = phone_pool[i]
		client.email = email_pool[i]
		client.status = get_status()

		clients.append(client)

	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for c in clients:
			f.write(to_line(c.first_name, c.last_name, c.sex, c.phone, c.email, c.status))


if __name__ == "__main__":
	generate_clients(1000, "client.csv")
