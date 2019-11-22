--#11 Создание новой временной локальной таблицы из результирующего набора данных инструкции SELECT.
-- Временная таблица с кассирами, обслужившими наибольшее число покупателей в 2018
select e.id, e.first_name, e.last_name, count(*) as served
into temp best_cashiers
from employee e
join orders o on e.id = o.cashier_id
where o.order_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59'
group by e.id, e.first_name, e.last_name
order by served desc
limit 30;
