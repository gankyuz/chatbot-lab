from src.ai.sql_generator import generate_sql
from src.db.execute import execute_sql

def main():
    
    print("=== Chat SQL com LLM ===")
    
    while True:
    
        question = input("\nPergunta:")

        if question.lower() == "sair":
            break
           
           
        try: 
            sql = generate_sql(question)


            print("SQL GERADO:")
            print(sql)

            result = execute_sql(sql)

            print("\nRESULTADO:")
            print(result)
            
        except Exception as e:
            print(f"\nErro: {e}")

    
    
if __name__ == "__main__":
    main()