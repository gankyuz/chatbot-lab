import psycopg2 as pg
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conn():
    try:
        pwd = os.getenv("POSTGRES_PASSWORD")
        usr = os.getenv("POSTGRES_USER")
        prt = os.getenv("POSTGRES_PORT")
        db = os.getenv("POSTGRES_DB")
        
        conecta = pg.connect(
            user=usr,
            password=pwd,
            host="localhost",
            port=prt,
            database=db
        )
        
        print("Conectado com sucesso!")
        
        return conecta

    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar no banco de : {e}")
        
def encerra_conn(conecta):
    if conecta:
        conecta.close()
        print("Conexão encerrada.")