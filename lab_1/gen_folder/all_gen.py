from product_gen import generate_product
from store_gen import generate_store
from client_gen import generate_client
from stock_gen import generate_stock
from employee_gen import generate_employee
from order_gen import generate_order
from order_product_gen import generate_order_product
from time import time


def generate_all(amount, product_db, store_db, client_db, job_db, stock_db, employee_db, order_db, order_product_db):
	beg = time()
	generate_product(amount, product_db)
	print("PRODUCT", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_store(amount, store_db)
	print("STORE", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_client(amount, client_db)
	print("CLIENT", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_stock(stock_db, product_db, store_db)
	print("STOCK", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_employee(amount, employee_db, store_db, job_db)
	print("EMPLOYEE", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_order(amount * 5, order_db, client_db, store_db, employee_db)
	print("ORDER", '{:.2f}'.format(time() - beg))

	beg = time()
	generate_order_product(order_product_db, order_db, product_db)
	print("ORDER_PRODUCT", '{:.2f}'.format(time() - beg))


if __name__ == "__main__":
	generate_all(1000, "product.csv", "store.csv", "client.csv", "job.csv", "stock.csv", "employee.csv", "order.csv", "order_product.csv")

#\i 'S:/GitHub/Databases/lab_1/create.sql'
#\i 'S:/GitHub/Databases/lab_1/insert.sql'
