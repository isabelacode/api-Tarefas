# API To-Do List
Apresento um projeto de uma API de lista de tarefas construída utilizando Django e Django Rest Framework, complementada por uma interface desenvolvida em JavaScript, HTML e CSS.

## Funcionalidades
- CRUD (Criar, Ler, Atualizar, Deletar): Implementa operações completas para gerenciar tarefas.
- Marcar como concluída: Permite aos usuários marcar tarefas como concluídas para acompanhar seu progresso.
- Filtragem por usuário: Facilita a visualização de tarefas específicas associadas a cada usuário.
- Adicionar e Remover Tarefas: Oferece a capacidade de adicionar novas tarefas ou remover aquelas que não são mais necessárias.
- Interface Interativa: Integra uma interface dinâmica que interage de forma transparente com o backend, proporcionando uma experiência suave e responsiva para os usuários.


## Instalação
1. Clone este repositório:
````git clone https://github.com/isabelacode/api-Tarefas.git````


2. Preparando o projeto:
 -  Navegue até a pasta do projeto

-  Crie um ambiente virtual com o comando:
  ````python3 -m venv venv````

- Instale as dependências:
````pip install -r requirements.txt````

- Ative a venv com o comando
````source venv/bin/activate  # Para Linux/Mac````
````venv\Scripts\activate.bat  # Para Windows````

3. Configurar o banco de dados postgres

-  Crie uma tabela chamada “toDoList”  no PostgreSQL.
-  Modifique a configuração do banco de dados no arquivo settings.py para inserir sua própria senha.


4. Execute as migrações do Django:
````python manage.py migrate````

5. Inicie o servidor de desenvolvimento:
````python manage.py runserver````

A API estará disponível em http://localhost:8000/


## Endpoints
- **GET /tarefas/:** Retorna todas as tarefas.
- **POST /tarefas/:** Cria uma nova tarefa.
- **GET /tarefas/:id/:** Retorna detalhes de uma tarefa específica.
- **PUT /tarefas/:id/:** Atualiza os detalhes de uma tarefa específica.
- **DELETE /tarefas/:id/:** Deleta uma tarefa específica.
- **POST /tarefas/:id/concluida/:** Marca uma tarefa como concluída.

## Urls da interface

 -  **cadastro:**  http://127.0.0.1:8000/auth/cadastro/
 -  **login:**  http://127.0.0.1:8000/auth/login/
 -  **home:**  http://127.0.0.1:8000/auth/home/
 -  **logout:**  http://127.0.0.1:8000/auth/logout/




