--#23 Инструкция SELECT, использующая рекурсивное обобщенное табличное выражение.
-- ???
with recursive mult3(n) as
(
	select 3
	union all
	select n+3 from mult3
	where n < 300
)
select n from mult3;
