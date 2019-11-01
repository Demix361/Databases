drop table if exists product cascade;

create table if not exists product (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost money not null
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
	store_id int not null,
	product_id varchar(10) not null,
	quantity int not null
);


drop table if exists employee cascade;

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


drop table if exists purchase cascade;

create table if not exists purchase (
	client_id int references client(id),
	product_id varchar(10) references product(id),
	store_id int references store(id),
	amount int not null,
	purchase_time varchar(20) not null
);


alter table store
ADD CONSTRAINT postal_code CHECK (postal_code > 0);

--\i 'S:/GitHub/Databases/lab_1/create.sql'
--insert into job values('Грузчик', 300000);