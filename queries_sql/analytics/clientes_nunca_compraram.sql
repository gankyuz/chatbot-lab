select clientes.nome 
from clientes
left join pedidos
on clientes.id = pedidos.cliente_id
where cliente_id is null