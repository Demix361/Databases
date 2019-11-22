--#5 Инструкция SELECT, использующая предикат EXISTS с вложенным подзапросом.
--Покупатели, которые совершили покупки 31 декабря
select first_name, last_name
from client c
where exists (
	select 1
	from orders o
	where o.client_id = c.id and
	o.order_time between '2019-12-31 00:00:00' and '2019-12-31 23:59:59'
)
order by first_name, last_name;
