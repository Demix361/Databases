from random import randint, choice
from translate import Translator


class Item():
	def __init__(self):
		self.category = None
		self.name = None
		self.price = None
		self.index = None
		self.color = None


def get_color():
	color_pool = ["black", "white", "pink", "yellow", "gold", "light red",
	"turquoise", "olive drab", "orchid", "brown", "orange", "purple",
	"light blue", "sandy brown", "spring green", "maroon", "gray", "red",
	"blue", "green", "light cyan", "chocolate", "salmon", "ivory", "white", 
	"dark_red", "dark_blue", "silver", "aquamarine", "dark green", "violet red",
	"wheat"]

	return choice(color_pool)


def get_index():
	first = randint(100, 999)
	mid = randint(100, 999)
	last = randint(10, 99)

	return str(first) + "." + str(mid) + "." + str(last)


def get_price():
	return randint(5, 200) * 100 - 1


def get_name():
	tr = Translator(to_lang="sv")
	return tr.translate("father")



def generate_items(amount, filename):
	items = []
	secret = '<your secret from Microsoft>'
	tr = Translator(provider='microsoft', to_lang="sv", secret_access_key=secret)

	for i in range(10):
		print(tr.translate("father"))




generate_items(100, "ikea.txt")

	

