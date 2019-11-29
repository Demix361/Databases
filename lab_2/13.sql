--#13 Инструкция SELECT, использующая вложенные подзапросы с уровнем вложенности 3.
--Все магазины, в которых покупали товар с названием 'skörda'
select *
from store s
where s.id in
(
	select e.store_id
	from employee e
	join orders o on e.id = o.cashier_id
	where o.id in
	(
		select op.order_id
		from order_product op
		join product p2 on op.product_id = p2.id
		where p2.id =
		(
			select p.id
			from product p
			where p.name = 'skörda'
		)
	)
);
