select produto, count(*) as vendas
from pedidos
group by produto
order by vendas desc
limit 1