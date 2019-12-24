create database rk3;

--1 1 - в питоне используя библиотеку и курсор пихаем в екзккьют большой запрос.

drop table if exists visits;
create table if not exists visits (
    emp_id int not null,
	date_visit date not null,
	day_week varchar(20) not null,
	time_visit time not null,
	visit_type int not null,
	primary key (emp_id, date_visit, time_visit)
);

drop table if exists employees;
create table if not exists employees (
    id int not null primary key,
	name varchar(100) not null,
	birth_date date not null,
	department varchar(50)
);

insert into visits(emp_id, date_visit, day_week, time_visit, visit_type) values
(1, '14-12-2018', 'Суббота', '9:00', 1),
(1, '14-12-2018', 'Суббота', '9:20', 2),
(1, '14-12-2018', 'Суббота', '9:25', 1),
(2, '14-12-2018', 'Суббота', '9:05', 1);

insert into employees(id, name, birth_date, department) values
(1, 'Иванов Иван Иванович', '25-09-1990', 'ИТ'),
(2, 'Петров Петр Иванович', '12-11-1987', 'Бухгалтерия');

--1 задание
create or replace function rk_f() returns double precision as
$$
    select avg(date_part('year', '21-12-2019'::date) - date_part('year', e.birth_date))
    from visits v
    join employees e on e.id = v.emp_id
    join (
        select emp_id, min(v2.time_visit) as f_visit_time
        from visits v2
        group by emp_id
        ) as first_visit on first_visit.emp_id = e.id
    where first_visit.f_visit_time > '9:00'

$$ language sql;

select rk_f();
