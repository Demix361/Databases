create table if not exists product (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost money not null
);

COPY product(id, name, category, color, cost) 
FROM 'S:\GitHub\Databases\lab_1\gen_folder\product.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
