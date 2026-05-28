from fastapi import FastAPI

from src.ai.sql_generator import generate_sql
from src.db.execute import execute_sql

#instacia aplicação web
app = FastAPI()

#define um rota get
@app.get("/")
def home():
    return {
        "message": "API funcionando!"
    }


#define uma rota post
@app.post("/chat")
def chat(question : str): #api recebe uma questão em string
    
    sql = generate_sql(question) #gera sql
    result = execute_sql(sql) #executa sql
    
    #executa resposta
    return { 
        "question": question,
        "sql": sql,
        "result": result
    }
