import psycopg2 as pg
from psycopg2 import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conn():
    try:
        pwd = os.getenv("db_password")
        
        conecta = pg.connect(
            user="admin",
            password=pwd,
            host="localhost",
            port=5433,
            database="chatbot_db"
        )
        
        print("Conectado com sucesso!")
        
        return conecta

    except Error as e:
        print(f"Ocorreu um erro ao tentar conectar no banco de : {e}")
        
def encerra_conn(conecta):
    if conecta:
        conecta.close()
        print("Conexão encerrada.")