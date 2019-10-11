from item_generator import generate_items
from store_generator import generate_stores
from stock_generator import generate_stock
from customer_generator import generate_customers


def generate_all(f_item, f_store, f_stock, f_customer, amount):
	generate_items(amount, f_item)
	generate_stores(amount, f_store)
	generate_stock(f_stock, f_item, f_store)
	generate_customers(amount, f_customer, f_item, f_store)


if __name__ == "__main__":
	generate_all("items.txt", "stores.txt", "stock.txt", "customers.txt", 1000)