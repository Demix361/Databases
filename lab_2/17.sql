--#17 Многострочная инструкция INSERT, выполняющая вставку в таблицу результирующего набора данных вложенного подзапроса.
-- Устраиваем на работу покупателей, сделавших заказы 31 декабря 2019
insert into employee(first_name, last_name, sex, phone, email, store_id, job_id)
select c.first_name, c.last_name, c.sex, c.phone, c.email, 1, 1
from orders o
join client c on o.client_id = c.id
where o.order_time between '2019-12-31 00:00:00' and '2019-12-31 23:59:59';
