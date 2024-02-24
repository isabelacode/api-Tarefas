# API To-Do List
Este é um exemplo de uma API de lista de tarefas desenvolvida usando Django e Django Rest Framework.

## Funcionalidades
- CRUD (Criar, Ler, Atualizar, Deletar) operações para tarefas.
- Marcar uma tarefa como concluída.
- Filtragem de tarefas por usuário.

## Instalação
1. Clone este repositório:
````git clone https://github.com/isabelacode/api-Tarefas.git````


2. Preparando o projeto:
   
- Entre na pasta onde está o projeto
- Instale o venv com o comando
  ````python3 -m venv venv````
- Instale as dependências:
````pip install -r requirements.txt````
- Ative a venv com o comando
````source venv/bin/activateou pelo windows venv\Scripts\activate.bat.````

3. Configurar o banco de dados postgres

- criar uma tabela chamada toDoList dentro do postgres, e modificar para sua senha propria dentro de settings.py

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
