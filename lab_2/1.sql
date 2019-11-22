--#1 Инструкция SELECT, использующая предикат сравнения.
--Названия всех красных предметов, цена которых ниже 10000
select name, color, cost from product
where product.color = 'red' and product.cost < 10000;
