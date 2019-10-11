from random import randint, choice


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


def get_names_pool(filename):
	names = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			word = line[:-1]
			names.append(word.lower())

	return names


def get_name(names_pool):
	return choice(names_pool)


def get_category():
	categories = ["Bed", "Sofa-bed", "Mattresses", "Wardrobes", "Chest of drawer", "other furniture",
	"Bedside table", "Dressing table", "Bedding", "Quilt", "Pillow", "Mattress", "Pillow protector",
	"Blanket", "Throw", "Bedspread", "Sofa", "Armchair", "Coffee table", "Side table", "Curtains",
	"Bedroom storage", "Clothes organiser", "Underbed storage", "Mirror", "Bedroom lighting",
	"Open storage system", "Sorting solution", "Bedroom decoration", "Accessories",
	"TV Stand", "Media Unit", "Shelving unit", "Bookcase", "Cabinet", "Living Room Lighting",
	"Wall shelve", "Home furnishing rug", "Kitchen", "Kitchen appliance", "Cookware", "Food storage",
	"Dining table", "Dining seating", "Dinnerware", "Glassware", "Cutlery", "Serveware",
	"Kitchen lighting", "Vanity unit", "Bathroom Sink", "Bathroom accessories", "Bathroom tap",
	"Shower", "Towel", "Shower curtains", "Bathroom lighting", "Bathroom decoration", "Office desk"]

	return choice(categories)

def get_str(item):


def generate_items(amount, filename):
	items = []
	names_pool = get_names_pool("swe_nouns.txt")

	for i in range(amount):
		item = Item()
		item.name = get_name(names_pool)
		item.price = get_price()
		item.color = get_color()
		item.category = get_category()
		item.index = get_index()


	with open(filename, "a") as f:
		for item in items:
			f.write(get_str(item))




generate_items(100, "ikea.txt")

	

