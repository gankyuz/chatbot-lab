from faker import Faker
import psycopg
import random

fake = Faker('pt-BR')

conn = psycopg.connect(
    host="localhost",
    dbname="chatbot_db",
    user="admin", 
    password="admin",
    port=5433
)

cur = conn.cursor()

for i in range(100):
    
    nome = fake.name()
    cidade = fake.city()
    email = fake.email()
    
    cur.execute(
        
        """
        insert into clientes (nome, cidade, email) values (%s, %s, %s)
        """,
        (nome, cidade, email)
        
    )
    
produtos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "SSD",
    "Headset",
    "Cadeira Gamer",
    "Webcam"
]

cur.execute("SELECT id FROM clientes")

clientes_ids = [row[0] for row in cur.fetchall()]

for i in range(300):
    cliente_id = random.choice(clientes_ids)
    produto = random.choice(produtos)
    valor = round(random.uniform(100,5000), 2)
    data_pedido = fake.date_time_this_year()
    
    cur.execute(
        """
        insert into pedidos (cliente_id, produto, valor, data_pedido) values (%s,%s,%s,%s)
        """,
        
        (cliente_id, produto, valor, data_pedido)
        
    )
    
for i in range(1000):
    cliente_id = random.choice(clientes_ids)
    ip = fake.ipv4()
    sucesso = random.choice([True, False])
    data_login = fake.date_time_this_year()
    
    cur.execute(
        """
        insert into login_logs (cliente_id, ip, sucesso, data_login) values (%s,%s,%s,%s)
        """,
        
        (cliente_id, ip, sucesso, data_login)
    )
    
conn.commit()
cur.close()
conn.close()

print("Banco populado")