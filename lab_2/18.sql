--#18 Простая инструкция UPDATE
-- Перевод всех сотрудников, кроме кассиров из магазина 1 в магазин 2
update employee
set employee.store_id = 2
where employee.store_id = 1 and
      employee.job_id != 1 or employee.job_id != 2;
