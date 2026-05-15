select produto, avg(valor) as ticket_medio
from pedidos
group by produto
order by ticket_medio desc