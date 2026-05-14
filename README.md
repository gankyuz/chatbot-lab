# Chatbot Lab

Projeto de estudo para construção de um chatbot integrado a banco de dados relacional, analytics e modelos de linguagem.

---

## Introdução

O Chatbot Lab é um ambiente de aprendizado prático que evolui gradualmente até um chatbot capaz de consultar tabelas PostgreSQL e responder perguntas em linguagem natural. O projeto cobre desde a infraestrutura com Docker até a integração com LLMs.

---

## Motivação

- Entender na prática a integração entre serviços via Docker
- Aprender como bancos relacionais funcionam com persistência e backup
- Explorar análise de dados com ferramentas BI
- Estudar geração automática de SQL e analytics conversacional
- Experimentar com copilotos de dados e integração com LLMs

---

## Stack

| Camada | Tecnologias |
|---|---|
| Infraestrutura | Docker, Docker Compose |
| Banco de Dados | PostgreSQL, pgAdmin |
| Analytics | Metabase |
| Backend / Scripts | Python, psycopg, Faker |
| Futuras integrações | FastAPI, OpenAI SDK, OpenRouter, LM Studio, PandasAI |

---

## Como rodar o projeto

### Subir os containers

```bash
docker compose up -d
```

---

## Backup
 
### Criar backup
 
```powershell
docker exec -t postgres_estudo pg_dump -U admin chatbot_db > backup\chatbot_db.sql
```
 
### Restaurar backup
 
```powershell
Get-Content backup\chatbot_db.sql | docker exec -i postgres_estudo psql -U admin -d chatbot_db
```
 
---
### Serviços

| Serviço | Porta | Acesso | Finalidade |
|---|---|---|---|
| PostgreSQL | 5433 | — | Banco de dados |
| pgAdmin | 5050 | http://localhost:5050 | Administração do banco |
| Metabase | 3000 | http://localhost:3000 | Dashboards e analytics |

### Credenciais padrão

**pgAdmin:** `admin@email.com` / `admin`

**PostgreSQL (pgAdmin e Metabase):**

| Campo | Valor |
|---|---|
| Host | postgres |
| Port | 5432 |
| Database | chatbot_db |
| Username | admin |
| Password | admin |

---

## Progresso

### ✅ Concluído

- Ambiente Docker com PostgreSQL, pgAdmin e Metabase integrados
- Banco relacional criado com tabelas e relacionamentos
- Persistência configurada via volumes Docker
- Backup e restauração do banco PostgreSQL
- Integração Python + PostgreSQL com psycopg v3
- Geração de dados sintéticos com Faker
- Primeiras consultas SQL e estudos de analytics

### 🔲 Próximos passos

- FastAPI
- Integração com OpenAI SDK / OpenRouter / LM Studio
- Geração automática de SQL
- Chatbot conversacional conectado ao banco
- Dashboards avançados e analytics com IA
- RAG com banco de dados

---

## Problemas enfrentados

**Conflito de porta PostgreSQL**
O PostgreSQL local do Windows ocupava a porta 5432. Solução: mapear o container para a porta 5433.

**Erro psycopg / psycopg2**
Incompatibilidade ao usar psycopg2. Solução: migrar para psycopg v3.

**Erro de Foreign Key**
Pedidos inseridos com `cliente_id` inexistente. Solução: buscar IDs reais da tabela `clientes` antes dos inserts.

---

## O que aprendi até agora

Docker · Docker Compose · containers · volumes · persistência · PostgreSQL · pgAdmin · Metabase · backup e restore · SQL relacional · foreign keys · integridade referencial · Python + PostgreSQL · Faker · analytics · troubleshooting
