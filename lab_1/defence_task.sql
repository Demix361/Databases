--названия таблиц, названия столбцов, тип данных

select table_name, column_name, data_type 
from information_schema.columns
where information_schema.columns.table_name in ('product', 'store', 'job', 'client', 'stock', 'employee', 'orders', 'order_product')
order by table_name;

