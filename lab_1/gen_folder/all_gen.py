from product_gen import generate_product
from store_gen import generate_store
from client_gen import generate_client
from stock_gen import generate_stock
from employee_gen import generate_employee
from purchase_gen import generate_purchase


def generate_all(amount, product_db, store_db, client_db, job_db, stock_db, employee_db, purchase_db):
	generate_product(amount, product_db)
	print("PRODUCT")
	generate_store(amount, store_db)
	print("STORE")
	generate_client(amount, client_db)
	print("CLIENT")
	generate_stock(stock_db, product_db, store_db)
	print("STOCK")
	generate_employee(amount, employee_db, store_db, job_db)
	print("EMPLOYEE")
	generate_purchase(amount * 10, purchase_db, client_db, product_db, store_db)
	print("PURCHASE")


if __name__ == "__main__":
	generate_all(1000, "product.csv", "store.csv", "client.csv", "job.csv", "stock.csv", "employee.csv", "purchase.csv")

#\i 'S:/GitHub/Databases/lab_1/code.sql'
#\i 'S:/GitHub/Databases/lab_1/drop.sql'
