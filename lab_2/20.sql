--#20 Простая инструкция DELETE.
-- Удаляет заказы, сделанные 1 января 2013 до 6 часов утра
delete from orders
where orders.order_time between '2013-01-01 00:00:00' and '2013-01-01 05:59:59';
