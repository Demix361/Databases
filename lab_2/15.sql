--#15 Инструкция SELECT, консолидирующая данные с помощью предложения GROUP BY и предложения HAVING.
-- Получить список категорий продуктов, средняя цена которых больше общей средней цены продуктов
select p.category, avg(p.cost) as avg_category_cost
from product p
group by p.category
having avg(p.cost) >
       (
            select avg(cost) as avg_cost
            from product
       );
