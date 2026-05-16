select clientes.nome, sum(pedidos.valor) as total
from clientes
join pedidos
on clientes.id = pedidos.cliente_id
group by clientes.nome
order by total desc
limit 1