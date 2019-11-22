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

