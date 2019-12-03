-- 1 Скалярная функция
-- Вывести количество предметов категории кровать на складах всех магазинов
create or replace function a1() returns int as
$$
    select sum(s.quantity)
    from stock s
    join product p on s.product_id = p.id
    where p.category = 'Bed'
$$ language sql;

select a1();


-- 2 Подставляемая табличная функция
-- Функция, принимает две даты, возвращает заказы, сделанные в этот промежуток
create or replace function orders_on_date(t1 timestamp, t2 timestamp) returns table
(
    id int,
    client_id int,
    store_id int,
    order_time timestamp
)
as
    $$
    select o.id, o.client_id, o.store_id, o.order_time
    from orders o
    where o.order_time between t1 and t2
    order by o.order_time;
    $$ language sql;

select *
from orders_on_date('2019-01-01 00:00:00', '2019-12-31 23:59:59');


-- 3 Многооператорная табличная функция
-- Вывести все заказы, в которых купили больше n товаров
create or replace function bought_greater_than(n int) returns table
(
    order_id int,
    client_id int,
    store_id int,
    order_time timestamp,
    item_amount bigint
) as
$$
    select distinct o.id as order_id, o.client_id, o.store_id, o.order_time, i_a_table.item_amount
    from orders o
    join order_product op on o.id = op.order_id
    join
    (
        select o2.id, sum(op2.amount) as item_amount
        from orders o2
        join order_product op2 on o2.id = op2.order_id
        group by o2.id
    ) as i_a_table on o.id = i_a_table.id
    where item_amount > n
    order by item_amount;
$$ language sql;

select *
from bought_greater_than(51);


-- 4 Рекурсивную функцию или функцию с рекурсивным ОТВ
-- Выводит иерархию магазинов и уровень в дереве
create or replace function output_store_tree() returns table
(
    store_id int,
    main_store_id int,
    level int
)
as
$$
    with recursive temp1 (store_id, main_store_id, level) as
    (
        select t1.store_id, t1.main_store_id, 1
        from store_hierarchy t1
        where t1.main_store_id is null
        union
        select t2.store_id, t2.main_store_id, level + 1
        from store_hierarchy t2 inner join temp1
        on (temp1.store_id = t2.main_store_id)
    )
    select  store_id, main_store_id, level
    from temp1;
$$ language sql;

select *
from output_store_tree();


-- 5 Хранимая процедура без параметров или с параметрами
-- Повышает n лучших кассиров до старших кассиров
select *
into temp employee_temp
from employee;

create or replace procedure raise_cashiers(n int) as
$$
    update employee_temp
    set job_id = 2
    from
    (
        select e.id as emp_id, count(o.id) as served
        from employee_temp e
        join orders o on o.cashier_id = e.id
        where e.id = 1
        group by e.id
        order by served desc
        limit n
    ) as best_cashiers
    where id = best_cashiers.emp_id;
$$ language sql;

call raise_cashiers(21);

select count(*)
from employee_temp et
where et.id = 2;


-- 6 Рекурсивная хранимая процедура или хранимая процедура с рекурсивным ОТВ
-- Обновить пол у всех клиентов в заданном диапазоне id
select *
into temp client_temp
from client;

create or replace procedure update_sex(beg_id int, end_id int, new_sex varchar(10)) as
$$
begin
    if (beg_id <= end_id)
    then
        update client_temp
        set sex = new_sex
        where id = beg_id;
        call update_sex(beg_id + 1, end_id, new_sex);
    end if;
end;
$$ language plpgsql;

call update_sex(1, 20, 'female');

select *
from client_temp
order by id;


-- 7 Хранимая процедура с курсором
--
