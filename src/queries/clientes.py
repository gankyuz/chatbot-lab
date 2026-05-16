#Quem gastou mais?
def top_clientes(cur):
    
    cur.execute(
        """
            select clientes.nome, sum(pedidos.valor) as total_gasto
            from clientes
            join pedidos
            on clientes.id = pedidos.cliente_id
            group by clientes.nome
            order by total_gasto desc
            limit 5
        
        """
        
    )
    
    resultado = cur.fetchall()
    return resultado

#Quais cidades possuem mais clientes?
def clientes_por_cidade(cur):

    cur.execute(
        """
            select cidade, count(*) as qtd
            from clientes
            group by cidade
            order by qtd desc
        """
        
    )
    
    resultado = cur.fetchall()
    return resultado
    
#Quais clientes nunca compraram?
def clientes_sem_pedidos(cur):
    
    cur.execute(
        """
            select clientes.nome 
            from clientes
            left join pedidos
            on clientes.id = pedidos.cliente_id
            where cliente_id is null
        """
    )
    resultado = cur.fetchall()
    return resultado
    
#Existe cliente com esse nome?
def buscar_cliente_por_nome(cur, nome):
    
    cur.execute(
        """
            select nome
            from clientes
            where nome = %s
        """,
        (nome,)
    )
    
    resultado = cur.fetchall()
    return resultado

#Quanto um cliente gastou?
def buscar_gasto_cliente(cur, cliente_id):
    
    cur.execute(
        """
            select clientes.nome, sum(pedidos.valor) as valor_gasto
            from clientes
            join pedidos
            on clientes.id = pedidos.cliente_id
            where clientes.id = %s
            group by clientes.nome
        """,
        (cliente_id,)
    )
    
    resultado = cur.fetchall()
    return resultado 
