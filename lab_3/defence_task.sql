-- Функция принимает на вход client_id, если он есть в orders, выводит информацию о клиенте

create or replace function get_client_info(c_id int) returns table
(
    id int,
	first_name varchar(50),
	last_name varchar(50),
	sex varchar(10),
	phone varchar(15),
	email varchar(50),
	status varchar(20)
)
as
$$
    select distinct c.id, c.first_name, c.last_name, c.sex, c.phone, c.email, c.status
    from orders o
    join client c on o.client_id = c.id
    where o.client_id = c_id
$$ language sql;

select *
from get_client_info(14);
