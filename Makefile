# Makefile para gerenciar o projeto Django com Docker

.PHONY: help db-up db-down db-logs migrate run-dev superuser clean

help: ## Mostra esta mensagem de ajuda
	@echo "Comandos disponíveis:"
	@echo "db-up           - Inicia o PostgreSQL"
	@echo "db-down         - Para o PostgreSQL" 
	@echo "db-logs         - Mostra logs do PostgreSQL"
	@echo "migrate         - Executa as migrações"
	@echo "run-dev         - Inicia servidor Django"
	@echo "superuser       - Cria superusuário"
	@echo "clean           - Remove containers e volumes"

db-up: ## Inicia o PostgreSQL
	docker compose -f docker-compose.db.yml up -d

db-down: ## Para o PostgreSQL
	docker compose -f docker-compose.db.yml down

db-logs: ## Mostra os logs do PostgreSQL
	docker compose -f docker-compose.db.yml logs -f

migrate: ## Executa as migrações
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py makemigrations
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py migrate

run-dev: ## Inicia servidor Django
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py runserver

superuser: ## Cria um superusuário
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py createsuperuser

clean: ## Remove containers, volumes e imagens
	docker compose -f docker-compose.db.yml down -v --rmi all

superuser: ## Cria um superusuário
	docker-compose exec web python manage.py createsuperuser

clean: ## Remove containers, volumes e imagens
	docker-compose down -v --rmi all

dev: ## Ambiente de desenvolvimento - para containers e inicia novamente
	make down && make up && make logs

install: ## Primeira instalação - constrói e inicia
	make build && make up
