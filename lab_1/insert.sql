COPY product(id, name, category, color, cost) 
FROM 'D:\GitHub\Databases\lab_1\gen_folder\product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY store(city, street, house, postal_code)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\store.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY client(first_name, last_name, sex, phone, email, status)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\client.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY job(position, salary)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\job.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY stock(store_id, product_id, quantity)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\stock.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY employee(first_name, last_name, sex, phone, email, store_id, job_id)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\employee.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY orders(client_id, store_id, cashier_id, order_time)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\order.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY order_product(order_id, product_id, amount)
FROM 'D:\GitHub\Databases\lab_1\gen_folder\order_product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
