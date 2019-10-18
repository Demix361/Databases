

from faker import Faker

fake = Faker()
for i in range(100):
	print(fake.job())
