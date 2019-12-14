-- 1 Task
--create database RK2;

drop table if exists supervisors cascade;
create table if not exists supervisors (
	id serial not null primary key,
	name varchar(100) not null,
	year_of_birth int not null,
	worked_for int not null,
	phone varchar(15) not null
);

drop table if exists clubs cascade;
create table if not exists clubs (
    id serial not null primary key,
    name varchar(100) not null,
    year int not null,
    description  text
);

drop table if exists visitors cascade;
create table if not exists visitors (
    id serial not null primary key,
    name varchar(100) not null,
    year_of_birth int not null,
    address varchar(200),
    email varchar(50)
);

drop table if exists sc cascade;
create table if not exists sc (
    supervisor_id int not null references supervisors(id) on delete cascade,
	club_id int not null references clubs(id) on delete cascade,
	primary key (supervisor_id, club_id)
);

drop table if exists cv cascade;
create table if not exists cv (
    visitor_id int not null references visitors(id) on delete cascade,
	club_id int not null references clubs(id) on delete cascade,
	primary key (visitor_id, club_id)
);

insert into supervisors(name, year_of_birth, worked_for, phone) values
('Алексеев Иван Антонович', 1956, 34, '+79165538790'),
('Игнатьев Ростислав Юрьевич', 1945, 45, '+79174569823'),
('Горшков Петр Петрович', 1967, 22, '+79247745389'),
('Анисимова Анастасия Егоровна', 1972, 12, '+77782834283'),
('Смирнов Артур Александрович', 1935, 6, '+79169823642'),
('Корнилова Ольга Артемовна', 1978, 31, '+79162837464'),
('Меркушева Тамара Ивановна', 1989, 10, '+79169234723'),
('Константинова Валерия Николаевна', 1963, 11, '+79169823487'),
('Кабанов Николай Павлович', 1969, 26, '+79168111233'),
('Комаров Максим Петрович', 1975, 18, '+79160984982');

insert into clubs(name, year, description) values
('Волейбол', 2002, 'Волейбольная секция для школьников'),
('Карате', 1993, '-'),
('Рисование', 2012, '-'),
('Музыкальный кружок', 2009, '-'),
('Бассейн', 2005, '-'),
('Бокс', 2008, '-'),
('Лепка из пластелина', 1993, '-'),
('Гончарное дело', 2016, '-'),
('Шитье', 2018, '-'),
('Футбол', 1999, '-');

insert into visitors(name, year_of_birth, address, email) values
('Логинов Дмитрий Иванович', 1999, 'ул. Ивана Бабушкина, 17 корпус 2, Москва, 117292', 'login.parol@gmail.com'),
('Блохин Михаил Александрович', 1997, 'Сумская ул., 6 корпус 3, Москва, 117208', 'asdfttt@yandex.ru'),
('Осокина Татьяна Дмитриевна', 2001, 'ул. Татищева, 11, Москва, 115191', 'osokggg@gmail.com'),
('Мишина Валерия Брьевна', 1989, 'ул. Донская, 14 корпус 1, Москва, 119049', 'posdfsdf@yandex.ru'),
('Шлыков Борис Всеволодович', 1990, 'Большой Могильцевский пер., 4, Москва, 119002', 'redsdjfsd@gmail.com'),
('Белых Ростислав Русланович', 1978, 'Столовый пер., 7А, Москва, 121069', 'uuuufsd@yahoo.ru'),
('Новиков Петр Петрович', 1992, 'ул. Красина, 27 строение 3, Москва, 123056', 'bjbbg34@ya.com'),
('Иванов Иван Иванович', 1998, 'Большой Сухаревский пер., 21 строение 2, Москва, 127051', 'buvbsd12@gmail.com'),
('Жданов Иван Нитрович', 2000, 'Большой Харитоньевский пер., 13, Москва, 105175', 'uuuuhu435@gmail.com'),
('Алексеев Алексей Ивановия', 2001, 'Большой Козловский пер., 11 стр 2, Москва, 107078', 'alek228@gmail.com');

insert into sc(supervisor_id, club_id) values
(1, 1),
(7, 2),
(6, 3),
(7, 4),
(8, 5),
(9, 6),
(2, 7),
(1, 8),
(5, 9),
(3, 10);

insert into cv(visitor_id, club_id) values
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 2),
(6, 2),
(7, 2),
(8, 2),
(9, 3),
(10, 3),
(1, 3),
(2, 4),
(3, 4),
(4, 5),
(5, 5),
(6, 6),
(7, 6),
(8, 6),
(9, 7),
(10, 7),
(1, 8),
(2, 8),
(4, 9),
(5, 9),
(6, 9),
(7, 10),
(8, 10),
(10, 10);


-- 2 Task
-- 1) Инструкция SELECT, использующая простое выражение CASE
select s.name, s.worked_for,
    case
        when s.worked_for >= 30 then 1
        when s.worked_for >= 20 then 2
        when s.worked_for >= 10 then 3
        when s.worked_for >= 5 then 4
    end as rang
from supervisors s;

-- 2) Инструкция, использующая оконную функцию
-- Вывести средний возраст посетителей кружка, руководитель которого имеет максимальный стаж
/*select distinct c.name, s.name, avg(2019 - v.year_of_birth) over (partition by sc.club_id)
from clubs c
join sc on c.id = sc.club_id
join supervisors s on sc.supervisor_id = s.id
join cv on cv.club_id = c.id
join visitors v on cv.visitor_id = v.id */
select distinct avg(2019 - v.year_of_birth) over (partition by club_id)
from visitors v
join cv on v.id = cv.visitor_id
join clubs c on cv.club_id = c.id

