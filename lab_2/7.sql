--#7 Инструкция SELECT, использующая агрегатные функции в выражениях столбцов.
-- Количества проданных продуктов
select order_product.product_id, p.name, p.category, sum(order_product.amount) as amount_sold
from order_product
join product p on order_product.product_id = p.id
group by order_product.product_id, p.category, p.name;
