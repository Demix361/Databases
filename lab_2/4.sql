--#4 Инструкция SELECT, использующая предикат IN с вложенным подзапросом.
--id покупок всех товаров в категории 'Кофейный столик', в 2019 году
select orders.id as order_id, product.name, product.category, orders.order_time
from orders
join order_product on orders.id = order_product.order_id
join product on order_product.product_id = product.id
where order_product.product_id in
(
	select id
	from product
	where category = 'Coffee table'
) and orders.order_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59'
order by orders.order_time;
