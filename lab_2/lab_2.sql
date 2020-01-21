--#1
--Названия всех красных предметов, цена которых ниже 10000
select name, color, cost from product
where product.color = 'red' and product.cost < 10000;


--#2
--Сотрудники с зарплатой от 20000 до 50000
select employee.first_name, employee.last_name, job.salary, job.position
from employee
join job on employee.job_id = job.id
where job.salary between 30000 and 40000;


--#3
--Все должности, в названии которых имеется слово 'менеджер'
select job.position
from job
where job.position like '%менеджер%';


--#4
--id покупок всех товаров в категории 'Кофейный столик', в 2019 году
select orders.id as order_id, product.name, product.category, orders.order_time
from orders
join order_product on orders.id = order_product.order_id
join product on order_product.product_id = product.id
where order_product.product_id in
(
	select id
	from product
	where category = 'Coffee table'
) and orders.order_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59'
order by orders.order_time;


--#5
--Покупатели, которые совершили покупки 31 декабря
select first_name, last_name
from client c
where exists (
	select 1
	from orders o
	where o.client_id = c.id and
	o.order_time between '2019-12-31 00:00:00' and '2019-12-31 23:59:59'
)
order by first_name, last_name;


--#6
-- Продукты, цена которых больше цены любого кресла
select *
from product
where cost > all (
	select cost
	from product
	where category = 'Armchair'
);


--#7 Инструкция SELECT, использующая агрегатные функции в выражениях столбцов.
-- Количества проданных продуктов
select order_product.product_id, p.name, p.category, sum(order_product.amount) as amount_sold
from order_product
join product p on order_product.product_id = p.id
group by order_product.product_id, p.category, p.name;


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


--#9 Инструкция SELECT, использующая простое выражение CASE
-- Клиенты, распределенные по статусу
select c.id, c.first_name, c.last_name,
	case status
		when 'diamond' then 20
		when 'gold' then 10
		when 'silver' then 5
		else 0
	end as discount
from client c;


--#10 Инструкция SELECT, использующая поисковое выражение CASE.
-- Сотрудники, распределенные по рангу зарплаты
select e.first_name, e.last_name, j.salary,
	case
		when j.salary < 30000 then 1
		when j.salary < 60000 then 2
		when j.salary < 90000 then 3
		else 4
	end as salary_class
from employee e
join job j on e.job_id = j.id;


--#11 Создание новой временной локальной таблицы из результирующего набора данных инструкции SELECT.
-- Временная таблица с кассирами, обслужившими наибольшее число покупателей в 2018
select e.id, e.first_name, e.last_name, count(*) as served
into temp best_cashiers
from employee e
join orders o on e.id = o.cashier_id
where o.order_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59'
group by e.id, e.first_name, e.last_name
order by served desc
limit 30;


--#12 Инструкция SELECT, использующая вложенные коррелированные подзапросы в качестве производных таблиц в предложении FROM.
-- Таблица с покупателями и продавцами, которые их обслуживали
select c.first_name as client_first_name,
       c.last_name as client_last_name,
       order_cashier.first_name as cashier_first_name,
       order_cashier.last_name as cashier_last_name,
       order_cashier.order_time
from client c join
(
	orders o join
	employee e on o.cashier_id = e.id
) as order_cashier on order_cashier.client_id = c.id
order by order_cashier.order_time;


--#13 Инструкция SELECT, использующая вложенные подзапросы с уровнем вложенности 3.
--Все магазины, в которых покупали товар с названием 'skörda'
select *
from store s
where s.id in
(
	select e.store_id
	from employee e
	join orders o on e.id = o.cashier_id
	where o.id in
	(
		select op.order_id
		from order_product op
		join product p2 on op.product_id = p2.id
		where p2.id =
		(
			select p.id
			from product p
			where p.name = 'skörda'
		)
	)
);


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


--#16 Однострочная инструкция INSERT, выполняющая вставку в таблицу одной строки значений.
-- Добавляем новую должность
insert into job(position, salary)
values('Помощник младшего уборщика', 9999);


--#17 Многострочная инструкция INSERT, выполняющая вставку в таблицу результирующего набора данных вложенного подзапроса.
-- Устраиваем на работу покупателей, сделавших заказы 31 декабря 2019
insert into employee(first_name, last_name, sex, phone, email, store_id, job_id)
select c.first_name, c.last_name, c.sex, c.phone, c.email, 1, 1
from orders o
join client c on o.client_id = c.id
where o.order_time between '2019-12-31 00:00:00' and '2019-12-31 23:59:59';


--#18 Простая инструкция UPDATE
-- Перевод всех сотрудников, кроме кассиров из магазина 1 в магазин 2
update employee
set employee.store_id = 2
where employee.store_id = 1 and
      employee.job_id != 1 or employee.job_id != 2;


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


--#20 Простая инструкция DELETE.
-- Удаляет заказы, сделанные 1 января 2013 до 12 часов
delete from orders
where orders.order_time between '2013-01-01 00:00:00' and '2013-01-01 11:59:59';


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


--#22 Инструкция SELECT, использующая простое обобщенное табличное выражение
-- Все кассиры, и сколько покупателей они обслужили
select e.id, e.first_name, e.last_name, count(*) as served
from employee e
join orders o on e.id = o.cashier_id
group by e.id
order by served desc;


--#23 Инструкция SELECT, использующая рекурсивное обобщенное табличное выражение.
-- Выводит иерархию магазинов и их уровень в дереве
with recursive temp1 (store_id, main_store_id, level) as (
    select t1.store_id, t1.main_store_id, 1
    from store_hierarchy t1
    where t1.main_store_id is null
    union
    select t2.store_id, t2.main_store_id, level + 1
    from store_hierarchy t2 inner join temp1
    on (temp1.store_id = t2.main_store_id)
)
select  * from temp1;


--#24 Оконные функции. Использование конструкций MIN/MAX/AVG OVER()
-- Товар, категория, цена, минимальная/максимальная/средняя цена в этой категории
select name, category, cost,
       min(cost) over (partition by category),
       max(cost) over (partition by category),
       avg(cost) over (partition by category)
from product;


--#25 Оконные функции для устранения дублей
select *
from
(
    select aa.name, row_number() over (partition by aa.name) as counter
    from product join
        (
            select *
            from stock join product on stock.product_id = product.id
            ) as aa on product.id = aa.id
    ) as percount
where counter = 1;
