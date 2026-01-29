# 🎬 MovieVerse API  
> Uma API REST moderna para cadastro e avaliação de filmes, desenvolvida com **Python**, **Django** e **Django Rest Framework (DRF)**.  
> Os usuários podem cadastrar filmes, gêneros e atores, além de avaliar os filmes com estrelas e comentários.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3.11.7**  
- 🌐 **Django 5.2.6**  
- ⚙️ **Django Rest Framework (DRF)**  
- 🔐 **JWT Authentication (SimpleJWT)**  
- 🗄️ **SQLite3** (pode ser substituído por PostgreSQL em produção)   
- 📦 **pip** para gerenciamento de dependências  

---

## 🧩 Estrutura da Aplicação

A API é composta pelos seguintes módulos principais:

| Módulo | Descrição |
|--------|------------|
| **users** | Gerenciamento de usuários e autenticação via JWT |
| **movies** | CRUD completo de filmes e gêneros |
| **actors** | Cadastro e listagem de atores |
| **reviews** | Sistema de avaliações com estrelas e comentários vinculados aos filmes |

---

## 🔑 Autenticação JWT

O sistema utiliza **JSON Web Tokens (JWT)** para autenticação de usuários.  
Após o login, o usuário recebe um **access token** e um **refresh token**, que devem ser usados para acessar rotas protegidas.

### Endpoints principais de autenticação:
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `POST` | `api/v1/authentication/token/` | Gera um novo par de tokens (login) |
| `POST` | `api//v1/authentication/token/refresh/` | Atualiza o access token expirado |

---

## 🎯 Principais Endpoints da API

### 🎞️ Filmes
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/movies/` | Lista todos os filmes |
| `POST` | `/api/v1/movies/` | Cria um novo filme |
| `GET` | `/api/v1/movies/{id}/` | Detalhes de um filme específico |
| `PUT` | `/api/v1/movies/{id}/` | Atualiza informações do filme |
| `DELETE` | `/api/v1/movies/{id}/` | Exclui um filme |

### 👤 Atores
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/actors/` | Lista todos os atores |
| `POST` | `/api/v1/actors/` | Cadastra um novo ator |
| `GET` | `/api/v1/actors/{id}/` | Detalhes de um ator específico |
| `PUT` | `/api/v1/actors/{id}/` | Atualiza informações do ator |
| `DELETE` | `/api/v1/actors/{id}/` | Exclui um ator |

### 🎭 Gêneros
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api/v1/genres/` | Lista todos os gêneros |
| `POST` | `/api/v1/genres/` | Cadastra um novo gênero |
| `GET` | `/api/v1/genres/{id}/` | Detalhes de um gênero específico |
| `PUT` | `/api/v1/genres/{id}/` | Atualiza informações do gênero |
| `DELETE` | `/api/v1/genres/{id}/` | Exclui um gênero |

### 🌟 Avaliações
| Método | Endpoint | Descrição |
|--------|-----------|-----------|
| `GET` | `/api//v1reviews/` | Lista todas as avaliações |
| `POST` | `/api/v1/reviews/` | Cria uma nova avaliação (necessita autenticação) |
| `GET` | `/api/v1/reviews/{id}/` | Detalha uma avaliação específica |

---

## ⚙️ Instalação e Configuração

### 🔧 1. Clone o repositório
```bash
# Clone esse repósitorio
git clone https://github.com/Francelmo87/flix_api_drf.git
# entre no projeto
cd flix_api_drf
# Crie sua venv
python -m venv .venv
# Ative sua venv(o comando é de acordo com seu S.O)     
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
# Instale as dependências
pip install -r requirements.txt
# Para Criar as variáveis de ambientes .env
python env_gen.py
# Faça as Migrações para o banco de Dados  
python manage.py migrate          
# Crie seu super usuário
python manage.py createsuperuser
# rode em sua máquina (acesse ao seu navegador)
python manage.py runserver
