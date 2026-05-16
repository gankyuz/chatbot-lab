select clientes.nome, count(*) as falhas
from clientes
join login_logs
on clientes.id = login_logs.cliente_id
where login_logs.sucesso = FALSE
group by clientes.nome
order by falhas desc