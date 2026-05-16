#Qual produto vende mais?
def produto_mais_vendido(cur):
    
    cur.execute(
        """
            select produto, count(*) as vendas
            from pedidos
            group by produto
            order by vendas desc
            limit 1
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Quanto o sistema faturou?
def faturamento_total(cur):
    
    cur.execute(
        """
            select sum(pedidos.valor) as faturamento_total
            from pedidos
            order by faturamento_total
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Qual o ticket médio?
def ticket_medio(cur):
    
    cur.execute(
        """
            select produto, avg(valor) as ticket_medio
            from pedidos
            group by produto
            order by ticket_medio desc
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Quais pedidos possuem valor acima de X?
def pedidos_maiores_que(cur, valor):

    cur.execute(
        """
            select * from pedidos
            where valor > %s
            order by valor desc
        """,
        (valor,)
    )
    
    resultado = cur.fetchall()
    return resultado

#Qual cidade gera mais dinheiro?
def faturamento_por_cidade(cur):
    
    cur.execute(
     """
        select clientes.cidade, sum(pedidos.valor) as faturamento
        from clientes
        join pedidos
        on clientes.id = pedidos.cliente_id
        group by clientes.cidade
        order by faturamento desc
     """
    )

    resultado = cur.fetchall()
    return resultado
    