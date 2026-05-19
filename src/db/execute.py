from src.db.connection import conn

def execute_sql(query):
    
    connection = conn()
    cur = connection.cursor()
    
    cur.execute(query)
    
    result = cur.fetchall()
    
    cur.close()
    connection.close()
    
    return result