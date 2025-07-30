@echo off
REM Script para gerenciar o projeto Django API Tarefas

set PYTHON_CMD=C:/Users/isabe/OneDrive/Documentos/Isa/api-Tarefas/.venv/Scripts/python.exe

if "%1"=="help" goto help
if "%1"=="install" goto install
if "%1"=="migrate" goto migrate
if "%1"=="run" goto run
if "%1"=="superuser" goto superuser
if "%1"=="shell" goto shell
if "%1"=="test" goto test
if "%1"=="collect" goto collect
if "%1"=="" goto run

:help
echo.
echo === API TAREFAS - COMANDOS DISPONIVEIS ===
echo.
echo install     - Instalar dependencias e configurar projeto
echo migrate     - Executar migracoes do banco de dados
echo run         - Iniciar servidor de desenvolvimento
echo superuser   - Criar superusuario
echo shell       - Abrir shell do Django
echo test        - Executar testes
echo collect     - Coletar arquivos estaticos
echo help        - Mostrar esta ajuda
echo.
goto end

:install
echo Instalando dependencias...
%PYTHON_CMD% -m pip install -r requirements.txt
echo Executando migracoes...
%PYTHON_CMD% manage.py migrate
echo Coletando arquivos estaticos...
%PYTHON_CMD% manage.py collectstatic --noinput
echo.
echo === INSTALACAO CONCLUIDA ===
echo Para iniciar o servidor: manage.bat run
echo Para criar superusuario: manage.bat superuser
echo.
goto end

:migrate
echo Criando migracoes...
%PYTHON_CMD% manage.py makemigrations
echo Aplicando migracoes...
%PYTHON_CMD% manage.py migrate
goto end

:run
echo Iniciando servidor de desenvolvimento...
echo.
echo === SERVIDOR RODANDO ===
echo API: http://localhost:8000/
echo Admin: http://localhost:8000/admin/
echo Tarefas API: http://localhost:8000/tarefas/
echo Auth API: http://localhost:8000/auth/
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
%PYTHON_CMD% manage.py runserver
goto end

:superuser
echo Criando superusuario...
%PYTHON_CMD% manage.py createsuperuser
goto end

:shell
echo Abrindo shell do Django...
%PYTHON_CMD% manage.py shell
goto end

:test
echo Executando testes...
%PYTHON_CMD% manage.py test
goto end

:collect
echo Coletando arquivos estaticos...
%PYTHON_CMD% manage.py collectstatic
goto end

:end
