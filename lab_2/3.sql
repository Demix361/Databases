--#3 Инструкция SELECT, использующая предикат LIKE.
--Все должности, в названии которых имеется слово 'менеджер'
select job.position
from job
where job.position like '%менеджер%';
