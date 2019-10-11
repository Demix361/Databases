from random import randint


a = []

def f(a):
	num = randint(0, 100)

	a.append(num)
	return num

for i in range(10):
	f(a)

print(a)