--#22 Инструкция SELECT, использующая простое обобщенное табличное выражение
-- Все кассиры, и сколько покупателей они обслужили
select e.id, e.first_name, e.last_name, count(*) as served
from employee e
join orders o on e.id = o.cashier_id
group by e.id
order by served desc ;
