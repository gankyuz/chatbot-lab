select cidade, count(*) as qtd
from clientes
group by cidade
order by qtd desc