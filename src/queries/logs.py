#Quais logins falharam?
def logins_falhos(cur):
    
    cur.execute(
        """
            select *
            from login_logs
            where sucesso = FALSE
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Quem falha mais login?
def usuarios_com_mais_falhas(cur):
    
    cur.execute(
        """
            select clientes.nome, count(*) as falhas
            from clientes
            join login_logs
            on clientes.id = login_logs.cliente_id
            where login_logs.sucesso = FALSE
            group by clientes.nome
            order by falhas desc
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Quais IPs acessam mais?
def ips_mais_ativos(cur):
    
    cur.execute(
        """
            select ip, count(*) as acessos
            from login_logs
            group by ip
            order by acessos desc
        """
    )
    
    resultado = cur.fetchall()
    return resultado

#Quantos logins existem?
def total_logins(cur):
    
    cur.execute(
        """
            select count(*) as total_logins
            from login_logs
            order by total_logins
        """
    )
    resultado = cur.fetchall()
    return resultado