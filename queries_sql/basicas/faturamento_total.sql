select sum(pedidos.valor) as faturamento_total
from pedidos
order by faturamento_total