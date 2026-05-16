select clientes.nome
from clientes 
inner join pedidos
on clientes.id = pedidos.cliente_id
where pedidos.id is NULL