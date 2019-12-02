from job_gen import generate_job
from product_gen import generate_product
from store_gen import generate_store
from client_gen import generate_client
from stock_gen import generate_stock
from employee_gen import generate_employee
from order_gen import generate_order
from order_product_gen import generate_order_product
from store_hierarchy import generate_store_hierarchy
from time import time


def generate_all(amount, product_db, store_db, client_db, job_db, stock_db, employee_db, order_db, order_product_db,
                 store_hierarchy_db):
    beg = time()
    generate_job(job_db)
    print("JOB", '{:.2f}'.format(time() - beg))

    beg = time()
    n = amount
    generate_product(n, product_db)
    print("PRODUCT", '{:.2f}'.format(time() - beg), n)

    beg = time()
    n = round(amount * 0.2)
    generate_store(n, store_db)
    print("STORE", '{:.2f}'.format(time() - beg), n)

    beg = time()
    n = amount * 10
    generate_client(n, client_db)
    print("CLIENT", '{:.2f}'.format(time() - beg), n)

    beg = time()
    generate_stock(stock_db, product_db, store_db)
    print("STOCK", '{:.2f}'.format(time() - beg))

    beg = time()
    n = amount * 30
    generate_employee(n, employee_db, store_db, job_db)
    print("EMPLOYEE", '{:.2f}'.format(time() - beg), n)

    beg = time()
    n = amount * 50
    generate_order(n, order_db, client_db, store_db, employee_db)
    print("ORDER", '{:.2f}'.format(time() - beg), n)

    beg = time()
    generate_order_product(order_product_db, order_db, product_db)
    print("ORDER_PRODUCT", '{:.2f}'.format(time() - beg))

    beg = time()
    generate_store_hierarchy(store_hierarchy_db, store_db)
    print("STORE_HIERARCHY", '{:.2f}'.format(time() - beg))


if __name__ == "__main__":
    generate_all(1000, "product.csv", "store.csv", "client.csv", "job.csv", "stock.csv", "employee.csv", "order.csv",
                 "order_product.csv", "store_hierarchy.csv")
