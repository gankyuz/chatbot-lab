select clientes.nome, count(*) as total_pedidos
from clientes
join pedidos
on clientes.id = pedidos.cliente_id
group by clientes.nome
order by total_pedidos desc