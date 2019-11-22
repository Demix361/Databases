--#2 Инструкция SELECT, использующая предикат BETWEEN.
--Сотрудники с зарплатой от 20000 до 50000
select employee.first_name, employee.last_name, job.salary, job.position
from employee
join job on employee.job_id = job.id
where job.salary between 30000 and 40000;
