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
