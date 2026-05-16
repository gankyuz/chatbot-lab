select clientes.nome, pedidos.produto, pedidos.valor
from clientes inner join pedidos
on clientes.id = pedidos.cliente_id