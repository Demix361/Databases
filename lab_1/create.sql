drop table if exists product cascade;

create table if not exists product (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost decimal(19, 4) not null
);


drop table if exists store cascade;

create table if not exists store (
	id serial not null primary key,
	city varchar(50) not null,
	street varchar(50) not null,
	house varchar(30) not null,
	postal_code int not null
);


drop table if exists client cascade;

create table if not exists client (
	id serial not null primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	sex varchar(10) not null,
	phone varchar(15) not null,
	email varchar(50) not null,
	status varchar(20) not null
);


drop table if exists job cascade;

create table if not exists job (
	id serial not null primary key,
	position varchar(200) not null,
	salary int not null
);


drop table if exists stock cascade;

create table if not exists stock (
	store_id int not null references store(id) on delete cascade,
	product_id varchar(10) not null references product(id) on delete cascade,
	quantity int not null,
	primary key (store_id, product_id)
);


drop table if exists employee cascade;

create table if not exists employee (
	id serial not null primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	sex varchar(10) not null,
	phone varchar(15) not null,
	email varchar(50) not null,
	store_id int references store(id) on delete cascade,
	job_id int references job(id) on delete cascade
);


drop table if exists orders cascade;

create table if not exists orders (
	id serial not null primary key,
	client_id int not null references client(id) on delete cascade,
	store_id int not null references store(id) on delete cascade,
	cashier_id int not null references employee(id) on delete cascade,
	order_time timestamp not null
);


drop table if exists order_product cascade;

create table if not exists order_product (
	order_id int not null references orders(id) on delete cascade,
	product_id varchar(10) not null references product(id) on delete cascade,
	amount int not null,
	primary key (order_id, product_id)
);


drop table if exists store_hierarchy;

create table if not exists store_hierarchy (
	store_id int not null references store(id) on delete cascade primary key,
    main_store_id int references store(id) on delete cascade
);


alter table store
ADD CONSTRAINT postal_code CHECK (postal_code > 0);
