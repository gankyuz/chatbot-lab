select clientes.nome, sum(pedidos.valor) as total_gasto
from clientes
join pedidos
on clientes.id = pedidos.cliente_id
group by clientes.nome
order by total_gasto desc