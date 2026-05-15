from ..db.connection import conn, encerra_conn

def main():
    connection = conn()
    
    encerra_conn(connection)
    
    
    
if __name__ == "__main__":
    main()