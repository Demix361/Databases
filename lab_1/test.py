from random import randint
from faker import Faker

f = Faker()

a = []

for i in range(1000):
	a.append(f.name())

with open("names.txt", "w") as f:
	for i in range(1000):
		f.write(a[i] + "\n")