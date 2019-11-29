--#21 Инструкция DELETE с вложенным коррелированным подзапросом в предложении WHERE.
-- Удаляет все заказы за январь 2013, в которых были товары из категории кофейные столики
delete from orders
where id in
(
    select op.order_id
    from order_product op
    join product p on op.product_id = p.id
    where p.category = 'Coffee table'
) and order_time between '2013-01-01 00:00:00' and '2013-01-31 23:59:59';
