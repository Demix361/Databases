from faker import Faker
from random import randint, choice


class Employee():
	def __init__(self):
		first_name = None
		last_name = None
		sex = None
		phone = None
		email = None
		store_id = None
		job_id = None


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


def get_store_amount(filename):
	i = 0

	with open(filename, "r") as f:
		for line in f:
			i += 1

	return i - 1


def get_job_amount(filename):
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


def generate_employee(amount, filename, store_db, job_db):
	employees = []
	male, female = get_name_pool(amount)
	phone_pool = get_phone_pool(amount)
	email_pool = get_email_pool(amount)
	store_amount = get_store_amount(store_db)
	job_amount = get_job_amount(job_db)
	table_header = "first_name,last_name,sex,phone,email,store_id,job_id\n"

	for i in range(amount):
		employee = Employee()

		if randint(0, 1) == 0:
			employee.last_name, employee.first_name = choice(male)
			employee.sex = "male"
		else:
			employee.last_name, employee.first_name = choice(female)
			employee.sex = "female"
		employee.phone = phone_pool[i]
		employee.email = email_pool[i]

		employee.store_id = randint(1, store_amount)
		employee.job_id = randint(1, job_amount)

		employees.append(employee)

	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for e in employees:
			f.write(to_line(e.first_name, e.last_name, e.sex, e.phone, e.email, e.store_id, e.job_id))


if __name__ == "__main__":
	generate_employee(1000, "employee.csv", "store.csv", "job.csv")
