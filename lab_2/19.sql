--#19 Инструкция UPDATE со скалярным подзапросом в предложении SET.
-- Меняет количество товара с идексом 205.859.26 во всех магазинах на среднее количество
update stock
set quantity =
        (
            select avg(quantity) :: int
            from stock
            where  product_id = '205.859.26'
            group by product_id
        )
where product_id = '205.859.26';
