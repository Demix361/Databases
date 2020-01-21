-- 1
-- Получение имени человека по id
create or replace function get_name_by_id(id_ int) returns varchar as
$$
    ppl = plpy.execute("select * from client")
    for person in ppl:
    	if person['id'] == id_:
    		return person['first_name']
    return 'None'
$$ language plpython3u;

select * from get_name_by_id(1003);
select * from get_name_by_id(1001);
select * from get_name_by_id(1);


-- 2
-- Сколько человек работает в заданном магазине
create or replace function get_n_food(id_s int) returns float as $$
    emp = plpy.execute("select * from employee")
    res = 0
    for e in emp:
	    if e['store_id'] == id_s:
		    res += 1
    return res
$$ language plpython3u;

select * from get_n_food(19);
select * from get_n_food(1);


-- 3
-- Возвращает всех людей указанного возраста
create or replace function get_clients_by_status (status varchar)
returns table (id int, first_name varchar, last_name varchar, sex varchar, phone varchar, email varchar, status varchar)
as $$
    ppl = plpy.execute("select * from client")
    res = []
    for p in ppl:
	    if p['status'] == status:
		    res.append(p)
    return res
$$ language plpython3u;

select * from get_clients_by_status('diamond');
select * from get_clients_by_status('gold');
select * from get_clients_by_status('bronze');


-- 4
-- Добавляет новый товар в базу
create or replace procedure add_product(id varchar, name varchar, category varchar, color varchar, cost decimal) as
$$
    plan = plpy.prepare("insert into product(id, name, category, color, cost) values($1, $2, $3, $4, $5);", ["varchar", "varchar", "varchar", "varchar", "decimal"])
    plpy.execute(plan, [id, name, category, color, cost])
$$ language plpython3u;

call add_product('000.000.01','new product', 'Bed', 'red', 1234);

select * from product
order by id;


-- 5
-- При удалении продуктов, данные копируются в таблицу product_old
drop table if exists product_old cascade;
create table if not exists product_old (
	id varchar(10) not null primary key,
	name varchar(50) not null,
	category varchar(50) not null,
	color varchar(30) not null,
	cost decimal(19, 4) not null
);

create or replace function backup_deleted_products()
returns trigger
as $$
    plan = plpy.prepare("insert into product_old(id, name, category, color, cost) values($1, $2, $3, $4, $5);", ["varchar", "varchar", "varchar", "varchar", "decimal"])
    pi = TD['old']
    rv = plpy.execute(plan, [pi["id"], pi["name"], pi["category"], pi["color"], pi["cost"]])
    return TD['new']
$$ language  plpython3u;

drop trigger backup_deleted_products on product;

create trigger backup_deleted_products
before delete on product for each row
execute procedure backup_deleted_products();

delete from product
where id = '000.000.01';

select * from product_old;


-- 6
-- Тип полного имени человека
create type fio as (
  first_name varchar,
  last_name varchar,
  sex varchar
);

-- Вывод полного имени человека по id
create or replace function get_fio_by_id(id_ integer) returns fio
as $$
    plan = plpy.prepare("select first_name, last_name, sex from client where id = $1", ["int"])
    cr = plpy.execute(plan, [id_])
    return (cr[0]['first_name'], cr[0]['last_name'], cr[0]['sex'])
$$ language plpython3u;

select * from get_fio_by_id(1001);

select *
from client
where id = 1001
