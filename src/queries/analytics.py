#Clientes que falham mais gastam mais?
def relacao_falhas_e_gastos(cur):
    
    cur.execute(
        """
            select clientes.nome, 
                count(
                    case 
                        when login_logs.sucesso = FALSE
                        then 1 
                    end) as falhas_login,
            sum(pedidos.valor) as total_gasto
            from clientes
            left join pedidos
            on clientes.id = pedidos.cliente_id
            left join login_logs
            on clientes.id = login_logs.cliente_id
            group by clientes.nome
            order by falhas_login, total_gasto desc
        """
    )
    
    resultado = cur.fetchall()
    return resultado
    
#Quem faz mais pedidos?
def clientes_mais_ativos(cur):
    
    cur.execute(
        """
            select clientes.nome, count(*) as mais_ativo
            from clientes
            join pedidos
            on clientes.id = pedidos.cliente_id
            group by clientes.nome
            order by mais_ativo desc
        """
    )
    
    resultado = cur.fetchall()
    return resultado