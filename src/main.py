from src.db.connection import conn, encerra_conn
from src.queries.clientes import (top_clientes, clientes_sem_pedidos)
from src.queries.pedidos import (produto_mais_vendido)

def main():
    
    connection = conn()
    cur = connection.cursor()
    
    while True:

        print("\n===== MENU =====\n")

        print("1 - Top clientes")
        print("2 - Clientes sem pedidos")
        print("3 - Produto mais vendido")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")


        if opcao == "1":

            resultado = top_clientes(cur)

            print("\nTOP CLIENTES:\n")

            for nome, valor in resultado:

                print(f"{nome} gastou R$ {valor:.2f}")


        elif opcao == "2":

            resultado = clientes_sem_pedidos(cur)

            print("\nCLIENTES SEM PEDIDOS:\n")

            for (nome,) in resultado:

                print(nome)


        elif opcao == "3":

            resultado = produto_mais_vendido(cur)

            print("\nPRODUTO MAIS VENDIDO:\n")

            for produto, total in resultado:

                print(f"{produto}: {total} vendas")


        elif opcao == "0":

            print("\nEncerrando sistema...")
            break


        else:

            print("\nOpção inválida.")
    
    
    cur.close()
    encerra_conn(connection)
    
    
    
if __name__ == "__main__":
    main()