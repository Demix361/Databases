create table if not exists product (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost money not null
);

COPY product(id, name, category, color, cost) 
FROM 'S:\GitHub\Databases\lab_1\gen_folder\product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists store (
	id serial not null primary key,
	city varchar(50) not null,
	street varchar(50) not null,
	house varchar(30) not null,
	postal_code int not null
);

COPY store(city, street, house, postal_code)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\store.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists client (
	id serial not null primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	sex varchar(10) not null,
	phone varchar(15) not null,
	email varchar(50) not null,
	status varchar(20) not null
);

COPY client(first_name, last_name, sex, phone, email, status)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\client.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists job (
	id serial not null primary key,
	position varchar(200) not null,
	salary int not null
);

COPY job(position, salary)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\job.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists stock (
	store_id int references store(id),
	product_id varchar(10) references product(id),
	quantity int not null
);

COPY stock(store_id, product_id, quantity)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\stock.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists employee (
	employee_id serial not null primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	sex varchar(10) not null,
	phone varchar(15) not null,
	email varchar(50) not null,
	store_id int references store(id),
	job_id int references job(id)
);

COPY employee(first_name, last_name, sex, phone, email, store_id, job_id)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\employee.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


create table if not exists purchase (
	client_id int references client(id),
	product_id varchar(10) references product(id),
	store_id int references store(id),
	amount int not null,
	purchase_time varchar(20) not null
);

COPY purchase(client_id, product_id, store_id, amount, purchase_time)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\purchase.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
