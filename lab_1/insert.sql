COPY product(id, name, category, color, cost) 
FROM 'S:\GitHub\Databases\lab_1\gen_folder\product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY store(city, street, house, postal_code)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\store.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY client(first_name, last_name, sex, phone, email, status)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\client.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY job(position, salary)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\job.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY stock(store_id, product_id, quantity)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\stock.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY employee(first_name, last_name, sex, phone, email, store_id, job_id)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\employee.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

COPY purchase(client_id, product_id, store_id, amount, purchase_time)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\purchase.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
