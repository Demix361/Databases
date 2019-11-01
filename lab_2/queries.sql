--\i 'S:/GitHub/Databases/lab_2/queries.sql'


--#1
--Названия всех красных предметов, цена которых ниже 10000
--select name, color, cost from product
--where product.color = 'red' and product.cost < 10000;

--#2
--Сотрудники с зарплатой от 20000 до 50000
select employee.first_name, employee.last_name, job.salary, job.position
from employee
join job on employee.job_id = job.id
where job.salary between 30000 and 40000

--#3
--