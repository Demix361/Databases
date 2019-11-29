--#24 Оконные функции. Использование конструкций MIN/MAX/AVG OVER()
-- Товар, категория, цена, минимальная/максимальная/средняя цена в этой категории
select name, category, cost,
       min(cost) over (partition by category),
       max(cost) over (partition by category),
       avg(cost) over (partition by category)
from product;
