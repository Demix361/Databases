from psycopg2 import connect
import psycopg2.extras


conn = connect(dbname='rk3', user='postgres',
               password='075743', host='localhost')

cursor1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor2 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor3 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor3.execute("""
select distinct e.department
from (
    select emp_id, min(v2.time_visit) as f_visit_time
    from visits v2
    group by emp_id, date_visit
    ) as first_visit
join employees e on e.id = first_visit.emp_id
where first_visit.f_visit_time <= '9:00';
""")

records = cursor3.fetchall()
print('\nЗадание 3')
print(records)

cursor2.execute("""
select e.id, e.name, left_during_work.times_left
from (
    select emp_id, count(*) as times_left
    from visits v2
    where v2.visit_type = 2
    and v2.time_visit between '9:00' and '18:00'
    group by emp_id
    ) as left_during_work
join employees e on e.id = left_during_work.emp_id
order by left_during_work.times_left desc;
""")

records = cursor2.fetchall()
print('\nЗадание 2')
print(records)

cursor1.execute("""
select distinct e.department
from (
         select first_visit.emp_id, count(*)
         from (
                  select emp_id, min(v2.time_visit) as f_visit_time, v2.date_visit
                  from visits v2
                  group by emp_id, v2.date_visit
              ) as first_visit
         where first_visit.f_visit_time > '9:00'
           and first_visit.date_visit between '2019-12-11' and '2019-12-21'
         group by first_visit.emp_id
     ) as asdf
join employees e on asdf.emp_id = e.id;
""")

records = cursor1.fetchall()
print('\nЗадание 1')
print(records)

cursor1.close()
cursor2.close()
cursor3.close()
conn.close()
