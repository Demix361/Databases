from random import randint, choice


class Product():
	def __init__(self):
		self.id = None
		self.name = None
		self.category = None
		self.color = None
		self.cost = None
	

def get_id_pool(amount):
	pool = []

	for i in range(amount):
		while True:
			first = randint(100, 999)
			mid = randint(100, 999)
			last = randint(10, 99)

			index = str(first) + "." + str(mid) + "." + str(last)

			if index not in pool:
				pool.append(index)
				break
	
	return pool


def get_name_pool(filename):
	names = []

	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			word = line[:-1]
			names.append(word.lower())

	return names


def get_cost():
	return randint(5, 200) * 100 - 1


def to_str(product):
	return product.id + "," + product.name + "," + product.category + "," + \
	product.color + "," + str(product.cost) + "\n"


def generate_products(amount, filename):
	products = []
	name_pool = get_name_pool("swe_nouns.txt") # unique
	id_pool = get_id_pool(amount) # unique
	table_header = "id,name,category,color,cost\n"

	color_pool = ["black", "white", "pink", "yellow", "gold", "light red",
	"turquoise", "olive drab", "orchid", "brown", "orange", "purple",
	"light blue", "sandy brown", "spring green", "maroon", "gray", "red",
	"blue", "green", "light cyan", "chocolate", "salmon", "ivory", "white", 
	"dark_red", "dark_blue", "silver", "aquamarine", "dark green", "violet red",
	"wheat"]

	category_pool = ["Bed", "Sofa-bed", "Mattresses", "Wardrobes", "Chest of drawer", "other furniture",
	"Bedside table", "Dressing table", "Bedding", "Quilt", "Pillow", "Mattress", "Pillow protector",
	"Blanket", "Throw", "Bedspread", "Sofa", "Armchair", "Coffee table", "Side table", "Curtains",
	"Bedroom storage", "Clothes organiser", "Underbed storage", "Mirror", "Bedroom lighting",
	"Open storage system", "Sorting solution", "Bedroom decoration", "Accessories",
	"TV Stand", "Media Unit", "Shelving unit", "Bookcase", "Cabinet", "Living Room Lighting",
	"Wall shelve", "Home furnishing rug", "Kitchen", "Kitchen appliance", "Cookware", "Food storage",
	"Dining table", "Dining seating", "Dinnerware", "Glassware", "Cutlery", "Serveware",
	"Kitchen lighting", "Vanity unit", "Bathroom Sink", "Bathroom accessories", "Bathroom tap",
	"Shower", "Towel", "Shower curtains", "Bathroom lighting", "Bathroom decoration", "Office desk"]

	for i in range(amount):
		product = Product()
		product.id = id_pool[i]
		product.name = choice(name_pool)
		product.category = choice(category_pool)
		product.color = choice(color_pool)
		product.cost = get_cost()
		
		products.append(product)


	with open(filename, "w", encoding="utf-8") as f:
		f.write(table_header)
		for p in products:
			f.write(to_str(p))


if __name__ == "__main__":
	generate_products(1000, "product.csv")