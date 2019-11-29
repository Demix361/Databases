--#12 Инструкция SELECT, использующая вложенные коррелированные подзапросы в качестве производных таблиц в предложении FROM.
-- Таблица с покупателями и продавцами, которые их обслуживали
select c.first_name as client_first_name,
       c.last_name as client_last_name,
       order_cashier.first_name as cashier_first_name,
       order_cashier.last_name as cashier_last_name,
       order_cashier.order_time
from client c join
(
	orders o join
	employee e on o.cashier_id = e.id
) as order_cashier on order_cashier.client_id = c.id
order by order_cashier.order_time;
