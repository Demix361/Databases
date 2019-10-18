create table if not exists product (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost money not null
);

--COPY product(id, name, category, color, cost) 
--FROM 'S:\GitHub\Databases\lab_1\gen_folder\product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

create table if not exists store (
	id serial not null primary key,
	city varchar(50) not null,
	street varchar(50) not null,
	house varchar(30) not null,
	postal_code int not null
);

COPY store(id, city, street, house, postal_code)
FROM 'S:\GitHub\Databases\lab_1\gen_folder\store.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';


