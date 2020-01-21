-- 1
select to_json(client) from client;
select row_to_json(client) from client;


-- 2
copy (select row_to_json(client) from client)
to 'S:\GitHub\Databases\lab_5\save.json';

create temp table client_import(doc json);
copy client_import from 'S:\GitHub\Databases\lab_5\save.json';

select p.*
from client_import, json_populate_record(null::client, doc) as p;

drop table client_import;

