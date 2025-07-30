.PHONY: help db-up db-down db-logs migrate run-dev superuser clean

help: 
	@echo "Comandos disponíveis:"
	@echo "db-up           - Inicia o PostgreSQL"
	@echo "db-down         - Para o PostgreSQL" 
	@echo "db-logs         - Mostra logs do PostgreSQL"
	@echo "migrate         - Executa as migrações"
	@echo "run-dev         - Inicia servidor Django"
	@echo "superuser       - Cria superusuário"
	@echo "clean           - Remove containers e volumes"

db-up:
	docker compose -f docker-compose.db.yml up -d

db-down: 
	docker compose -f docker-compose.db.yml down

db-logs: 
	docker compose -f docker-compose.db.yml logs -f

migrate:
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py makemigrations
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py migrate

run-dev: 
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py runserver

superuser: 
	C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe manage.py createsuperuser

clean: 
	docker compose -f docker-compose.db.yml down -v --rmi all

superuser: 
	docker-compose exec web python manage.py createsuperuser

clean: 
	docker-compose down -v --rmi all

dev: 
	make down && make up && make logs

install:
	make build && make up
