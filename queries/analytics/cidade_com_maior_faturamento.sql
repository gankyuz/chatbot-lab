select clientes.cidade, sum(pedidos.valor) as faturamento
from clientes
join pedidos
on clientes.id = pedidos.cliente_id
group by clientes.cidade
order by faturamento desc