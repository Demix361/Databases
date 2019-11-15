--\i 'S:/GitHub/Databases/lab_2/queries.sql'



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
select order_product.product_id, product.category,  
/*
select purchase.id, product.category, purchase.purchase_time
from purchase
join product on purchase.product_id = product.id
where purchase.product_id in
	(
		select id
		from product
		where category = 'Coffee table'
		) and purchase.purchase_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59';
*/
--#5
--Продукты, которые не покупали в 2019 году
select * 
from product
where not exists (
	select * 
	from purchase
	where product.id = purchase.product_id
	and purchase.purchase_time between '2019-01-01 00:00:00' and '2019-12-31 23:59:59'
);


--#6
-- Продукты, цена которых больше цены любого кресла
select *
from product
where cost > all (
	select cost
	from product
	where category = 'Armchair'
);


--#7
-- Количества проданных продуктов
select product.id, product.name, product.category, count(*) as sold_qty
from product join purchase
	on product.id = purchase.product_id
group by product.id;


--#8
--???


--#9
-- Клиенты, распределенные по статусу
select client.first_name, client.last_name,
	case status
		when 'diamond' then 4
		when 'gold' then 3
		when 'silver' then 2
		else 1
	end as rang
from client;


--#10
-- Сотрудники, распределенные по рангу зарплаты
select employee.first_name, employee.last_name, job.salary,
	case
		when job.salary < 30000 then 1
		when job.salary < 60000 then 2
		when job.salary < 90000 then 3
		else 4
	end as salary_rang
from employee
join job on employee.job_id = job.id;


--#11
-- Магазины, в которых есть сотрудники с максимальным рангом зарплаты
select store.*
into premium_store
from store
where id in (
	select store.id
	from store join (
		select store_id,
			case
				when job.salary < 30000 then 1
				when job.salary < 60000 then 2
				when job.salary < 90000 then 3
				else 4
			end as salary_rang
		from employee
		join job on employee.job_id = job.id
	) as m
		on store.id = m.store_id
		where m.salary_rang = '4'
);




--#12
-- 

