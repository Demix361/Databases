--#8 Инструкция SELECT, использующая скалярные подзапросы в выражениях столбцов.
-- Покупатели и средняя\минимальная стоимость их покупки
select c.id, c.first_name, c.last_name,
    (
        select avg(order_cost.cost)
        from
        (
            select o.client_id, sum(p.cost * op.amount) as cost
            from orders o
            join order_product op on o.id = op.order_id
            join product p on op.product_id = p.id
            group by o.id
        ) as order_cost
        where order_cost.client_id = c.id
    ) as avg_order_cost,
    (
        select min(order_cost.cost)
        from
        (
            select o.client_id, sum(p.cost * op.amount) as cost
            from orders o
            join order_product op on o.id = op.order_id
            join product p on op.product_id = p.id
            group by o.id
        ) as order_cost
        where order_cost.client_id = c.id
    ) as min_order_cost

from client c;
