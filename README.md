# Chatbot Lab

Projeto de estudo para construção de um chatbot integrado a banco de dados relacional, analytics e modelos de linguagem.

---

## Introdução

O Chatbot Lab é um ambiente de aprendizado prático que evolui gradualmente até um chatbot capaz de consultar tabelas PostgreSQL e responder perguntas em linguagem natural. O projeto cobre desde a infraestrutura com Docker até a integração com LLMs para geração automática de SQL.

---

## Motivação

- Entender na prática a integração entre serviços via Docker
- Aprender como bancos relacionais funcionam com persistência e backup
- Explorar análise de dados e analytics conversacional
- Estudar geração automática de SQL utilizando LLMs
- Experimentar integração entre banco de dados, Python e modelos de linguagem
- Desenvolver uma base para aplicações de chatbot com IA

---

## Stack

| Camada | Tecnologias |
|---|---|
| Infraestrutura | Docker, Docker Compose |
| Banco de Dados | PostgreSQL, pgAdmin |
| Analytics | Metabase |
| Backend / Scripts | Python, psycopg, Faker |
| IA / LLM | OpenAI SDK, OpenRouter |
| Processamento de Dados | Pandas |

---

## Arquitetura do Projeto

Pergunta em linguagem natural  
↓  
LLM via OpenRouter  
↓  
Geração automática de SQL  
↓  
Execução no PostgreSQL  
↓  
Retorno dos dados ao usuário

---

## Como rodar o projeto

### Subir os containers

```bash
docker compose up -d
```

---

### Instalar dependências Python

```bash
pip install -r requirements.txt
```

---

### Executar o chatbot

```bash
python -m src.main
```

---

## Backup

### Criar backup

```powershell
docker exec -t postgres_estudo pg_dump -U admin chatbot_db > backup\chatbot_db.sql
```

### Restaurar backup

```powershell
cmd /c "docker exec -i postgres_estudo psql -U admin -d chatbot_db < backup\chatbot_db.sql"
```

---

## Serviços

| Serviço | Porta | Acesso | Finalidade |
|---|---|---|---|
| PostgreSQL | 5433 | — | Banco de dados |
| pgAdmin | 5050 | http://localhost:5050 | Administração do banco |
| Metabase | 3000 | http://localhost:3000 | Dashboards e analytics |

---

## Credenciais padrão

### pgAdmin

```text
admin@email.com
admin
```

### PostgreSQL (pgAdmin e Metabase)

| Campo | Valor |
|---|---|
| Host | postgres |
| Port | 5432 |
| Database | chatbot_db |
| Username | admin |
| Password | admin |

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=chatbot_db
POSTGRES_PORT=5433
OPENROUTER_API_KEY=sua_chave
```

---

## Progresso

### ✅ Concluído

- Ambiente Docker com PostgreSQL, pgAdmin e Metabase integrados
- Banco relacional criado com tabelas e relacionamentos
- Persistência configurada via volumes Docker
- Backup e restauração do banco PostgreSQL
- Integração Python + PostgreSQL com psycopg v3
- Geração de dados sintéticos com Faker
- Consultas SQL e estudos de analytics
- Integração com OpenRouter via OpenAI SDK
- Geração automática de SQL com LLM
- Chat interativo conectado ao banco PostgreSQL
- Conversão de linguagem natural em queries SQL

### 🔲 Próximos passos

- API com FastAPI
- Interface web para o chatbot
- Melhor tratamento e formatação de respostas
- Memória de contexto para conversas
- Segurança e validação de queries SQL
- Integração com modelos locais (LM Studio)
- Dashboard analítico com IA

---

## Problemas enfrentados

### Conflito de porta PostgreSQL

O PostgreSQL local do Windows ocupava a porta 5432.

**Solução:** mapear o container para a porta 5433.

---

### Erro psycopg / psycopg2

Incompatibilidade ao utilizar psycopg2.

**Solução:** migração para psycopg v3.

---

### Erro de Foreign Key

Pedidos inseridos com `cliente_id` inexistente.

**Solução:** buscar IDs reais da tabela `clientes` antes dos inserts.

---

### Rate Limit em modelos gratuitos

Modelos gratuitos do OpenRouter apresentaram limitação temporária de uso.

**Solução:** troca dinâmica de modelos e testes com diferentes providers gratuitos.

---

## O que aprendi até agora

Docker · Docker Compose · PostgreSQL · pgAdmin · Metabase · volumes · persistência · backup e restore · SQL relacional · joins · group by · foreign keys · Python + PostgreSQL · Faker · OpenAI SDK · OpenRouter · integração com LLMs · geração automática de SQL · conversational analytics · troubleshooting
