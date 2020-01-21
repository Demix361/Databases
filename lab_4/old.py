import psycopg2


# 2 Агрегатная функция
# Вывести количество предметов заданной категории на складах всех магазинов
def q_2(cursor, category):
    cursor.execute(
        "select sum(s.quantity) " +
        "from stock s " +
        "join product p on s.product_id = p.id " +
        "where p.category = %s", (category,)
    )

    records = cursor.fetchall()
    return records


# 3 Табличная функция
# Функция, принимает две даты, возвращает заказы, сделанные в этот промежуток
def q_3(cursor, date_1, date_2):
    cursor.execute(
        "select o.id, o.client_id, o.store_id, o.order_time " +
        "from orders o " +
        "where o.order_time between %s and %s " +
        "order by o.order_time;", (date_1, date_2, )
    )

    records = cursor.fetchall()
    return records


# 4 Хранимая процедура
# Повышает n лучших кассиров до старших кассиров
def q_4(connect, cursor, amount):
    cursor.execute(
        "select * " +
        "into temp employee_temp " +
        "from employee;"
    )

    connect.commit()

    cursor.execute(
        "select count(*) " +
        "from employee_temp et " +
        "where et.job_id = 2;"
    )

    records = cursor.fetchall()

    cursor.execute(
        "update employee_temp " +
        "set job_id = 2 " +
        "from " +
        "( " +
            "select e.id as emp_id, count(o.id) as served " +
            "from employee_temp e " +
            "join orders o on o.cashier_id = e.id " +
            "where e.id = 1 " +
            "group by e.id " +
            "order by served desc " +
            "limit 20 " +
        ") as best_cashiers " +
        "where id = best_cashiers.emp_id;"
    )
    connect.commit()

    cursor.execute(
        "select count(*) " +
        "from employee_temp et " +
        "where et.job_id = 2;"
    )

    records += cursor.fetchall()

    return records


def main():
    conn = psycopg2.connect(
        user='postgres',
        password='',
        host='127.0.0.1',
        port='5432',
        database='test'
    )
    cursor = conn.cursor()

    #records = q_2(cursor, 'Bed')
    # records = q_3(cursor, '2019-12-01 00:00:00', '2019-12-31 23:59:59')

    records = q_4(conn, cursor, 30)
    for r in records:
        print(r)


    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
