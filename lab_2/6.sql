--#6 Инструкция SELECT, использующая предикат сравнения с квантором.
-- Товары, цена которых больше цены любого кресла
select *
from product
where cost > all (
	select cost
	from product
	where category = 'Armchair'
);
