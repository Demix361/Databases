--#14 Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY, но без предложения HAVING.
-- Средняя, минимальная, макссимальная стоимость заказа и количество заказов во всех магазинах
select s.id,
       avg(op.amount * p.cost) as avg_order_cost,
       min(op.amount * p.cost) as min_order_cost,
       max(op.amount * p.cost) as max_order_cost,
       count(s) as order_amount
from store s
join orders o on s.id = o.store_id
join order_product op on o.id = op.order_id
join product p on op.product_id = p.id
group by s.id;
