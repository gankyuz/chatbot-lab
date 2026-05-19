import pandas as pd
from src.db.connection import conn, encerra_conn


# transformando sql em dataframe

def clientes_dataframes():
    
    connection = conn()
    
    queries = """
        select clientes.nome, clientes.cidade, pedidos.produto, pedidos.valor, pedidos.data_pedido
        
        from clientes
        join pedidos
        on clientes.id = pedidos.cliente_id
        
    """
    
    df = pd.read_sql(queries, connection)
    
    connection.close

    return df