#  API To-Do List

> Uma API REST completa para gerenciamento de tarefas desenvolvida com Django e Django REST Framework, incluindo interface web interativa.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)

## Sobre o Projeto

Esta API de To-Do List oferece um sistema completo para gerenciamento de tarefas pessoais, permitindo que usuários criem, organizem e acompanhem suas atividades diárias. O projeto combina um backend robusto em Django.

### Principais Funcionalidades

- **Sistema de Usuários**: Cadastro e autenticação de usuários
- **CRUD Completo**: Criar, ler, atualizar e deletar tarefas
- **Controle de Status**: Marcar tarefas como concluídas/pendentes
- **Filtragem**: Visualizar tarefas por usuário e status
- **Timestamps**: Rastreamento de datas de criação e conclusão
- **Docker Ready**: Configuração completa com Docker Compose
- **API RESTful**: Endpoints bem estruturados seguindo padrões REST

## Início Rápido

### Pré-requisitos

-  **Docker** e **Docker Compose** (Recomendado)
- **Python 3.12+** (para instalação local)
- **PostgreSQL 15+** (para instalação local)
- **Git** para clonar o repositório

## Instalação com Docker (Recomendado)

### 1️. Clone o repositório
```bash
git clone https://github.com/isabelacode/api-Tarefas.git
cd api-Tarefas
```

### 2️. Configure as variáveis de ambiente
```bash
# Copie e configure o arquivo de ambiente
cp .env.example .env

# Edite o .env se necessário para suas configurações específicas
```

### 3. Execute com Docker Compose
```bash
# Construir e iniciar todos os serviços (recompila se houve mudanças)
docker-compose up --build

# Para executar em segundo plano
docker-compose up -d --build
```

### 4️. Execute as migrações iniciais
```bash
# Em outro terminal, execute as migrações
docker-compose exec web python manage.py migrate

# Criar um superusuário (opcional)
docker-compose exec web python manage.py createsuperuser
```

### 5️. Acesse a aplicação
-  **API**: http://localhost:8000/api/
- **Admin Django**: http://localhost:8000/admin/

###  Comandos úteis com Docker

```bash
# Ver logs em tempo real
docker-compose logs -f web

# Parar todos os serviços
docker-compose down

# Reiniciar completamente
docker-compose down && docker-compose up --build

# Acessar shell do Django
docker-compose exec web python manage.py shell

# Executar testes
docker-compose exec web python manage.py test
```

## Instalação Local (Desenvolvimento)

### 1️. Clone e prepare o ambiente
```bash
git clone https://github.com/isabelacode/api-Tarefas.git
cd api-Tarefas

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (CMD):
venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate
```

### 2️.  Instalar dependências
```bash
pip install -r requirements.txt
```

### 3️. Configurar banco de dados

**Opção A: PostgreSQL (Recomendado)**
```bash
# 1. Instale e configure PostgreSQL
# 2. Crie um banco de dados chamado 'toDoList'
# 3. Configure as credenciais no arquivo .env
```

**Opção B: SQLite (Desenvolvimento)**
```bash
# Edite o arquivo .env e descomente:
# DB_ENGINE=django.db.backends.sqlite3
```

### 4️. Executar migrações
```bash
python manage.py migrate
python manage.py createsuperuser  # Opcional
```

### 5️. Iniciar servidor de desenvolvimento
```bash
python manage.py runserver
```

##  Endpoints da API

### Tarefas
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `GET` | `/api/tarefas/` | Lista todas as tarefas do usuário | ✅ |
| `POST` | `/api/tarefas/` | Cria uma nova tarefa | ✅ |
| `GET` | `/api/tarefas/{id}/` | Detalhes de uma tarefa específica | ✅ |
| `PUT` | `/api/tarefas/{id}/` | Atualiza uma tarefa completa | ✅ |
| `PATCH` | `/api/tarefas/{id}/` | Atualiza parcialmente uma tarefa | ✅ |
| `DELETE` | `/api/tarefas/{id}/` | Remove uma tarefa | ✅ |

### Autenticação e Usuários (API REST)
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `POST` | `/auth/api/register/` | Criação de nova conta via API | ❌ |
| `POST` | `/auth/api/login/` | Login via API (retorna JWT) | ❌ |
| `GET` | `/auth/api/profile/` | Dados do usuário logado | ✅ |
| `POST` | `/auth/api/password-reset/` | Solicitar redefinição de senha | ❌ |
| `POST` | `/auth/api/password-reset-confirm/{uid}/{token}/` | Confirmar redefinição de senha | ❌ |
| `POST` | `/auth/api/token/refresh/` | Renovar token JWT | ❌ |
| `POST` | `/auth/api/token/verify/` | Verificar validade do token | ❌ |

### Interface Web (Templates)
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| `GET/POST` | `/auth/cadastro/` | Criação de nova conta | ❌ |
| `GET/POST` | `/auth/login/` | Login do usuário | ❌ |
| `GET` | `/auth/home/` | Página inicial (após login) | ✅ |
| `POST` | `/auth/logout/` | Logout do usuário | ✅ |
| `DELETE` | `/auth/delete-task/{id}/` | Remove uma tarefa (via web) | ✅ |

###  Estrutura do Modelo Tarefa
```json
{
  "id": 1,
  "titulo": "Estudar Django",
  "descricao": "Estudar Django REST Framework",
  "concluida": false,
  "data_criacao": "2025-01-15T10:30:00Z",
  "data_conclusao": null,
  "user": 1
}
```

###  Autenticação
```bash
# Exemplo de criação de conta via API
curl -X POST http://localhost:8000/auth/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "meuusuario",
    "email": "email@exemplo.com",
    "password": "minhasenha123",
    "password_confirmation": "minhasenha123",
    "first_name": "Meu",
    "last_name": "Nome"
  }'

# Exemplo de login via API
curl -X POST http://localhost:8000/auth/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "meuusuario",
    "password": "minhasenha123"
  }'

# Exemplo de solicitação de redefinição de senha
curl -X POST http://localhost:8000/auth/api/password-reset/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "email@exemplo.com"
  }'

# Exemplo de requisição autenticada com JWT
curl -H "Authorization: Bearer <access_token>" \
     -X GET http://localhost:8000/api/tarefas/

# Renovar token JWT
curl -X POST http://localhost:8000/auth/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "<refresh_token>"
  }'
```

## Tecnologias Utilizadas

### Backend
- **Python 3.12+** - Linguagem de programação
- **Django 5.0.2** - Framework web
- **Django REST Framework 3.14.0** - API REST
- **PostgreSQL 15** - Banco de dados principal
- **SQLite** - Banco de dados para desenvolvimento
- **Django Authentication** - Sistema de autenticação



### DevOps & Ferramentas
- **Docker & Docker Compose** - Containerização
- **pip** - Gerenciamento de dependências Python
- **python-decouple** - Gerenciamento de configurações
- **django-filter** - Filtragem avançada de dados


## Como Contribuir

1. **Fork** o projeto
2. **Clone** seu fork: `git clone https://github.com/seu-usuario/api-Tarefas.git`
3. **Crie** uma branch para sua feature: `git checkout -b feature/MinhaFeature`
4. **Faça** suas alterações e commit: `git commit -m 'Add: Minha nova feature'`
5. **Push** para a branch: `git push origin feature/MinhaFeature`
6. **Abra** um Pull Request


**Se este projeto foi útil para você, considere dar uma estrela!** 





