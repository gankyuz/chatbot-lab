from src.ai.sql_generator import generate_sql
from src.db.execute import execute_sql


while True:
    
    question = input("\nPergunta:")

    if question.lower() == "sair":
        break
        
    sql = generate_sql(question)


    print("SQL GERADO:")
    print(sql)

    try:
        result = execute_sql(sql)

        print("\nRESULTADO:")
        print(result)
        
    except Exception as e:
        print(f"\nErro ao executar SQL: {e}")
