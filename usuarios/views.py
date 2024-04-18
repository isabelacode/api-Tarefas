from tarefas.models import Tarefa
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.db.models import F 
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout 
from datetime import datetime

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if User.objects.filter(username=username).exists():
            mensagem_username = "Já existe um usuário com esse nome de usuário."
            return render(request, 'cadastro/index.html', {'mensagem_username': mensagem_username})
        elif User.objects.filter(email=email).exists():
            mensagem_email = "Já existe um usuário cadastrado com este endereço de e-mail."
            return render(request, 'cadastro/index.html', {'mensagem_email': mensagem_email})
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            return redirect('login')
        
def login(request):
    if request.method == "GET":
        return render(request, 'login/index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login_django(request,user)
            return home(request) 
        else:
            mensagem = "Usuario ou/e senha invalidos"
            return render(request, 'login/index.html', {'mensagem': mensagem})

@login_required(login_url="/auth/login/")
def home(request):
    if request.method == "POST":
        if "addTaskBtn" in request.POST: 
            titulo = request.POST.get("titulo")
            descricao = request.POST.get("descricao")
            if titulo and descricao: 
                user = request.user
                nova_tarefa = Tarefa.objects.create(user=user, titulo=titulo, descricao=descricao)
        elif "tarefas_concluidas" in request.POST:
            tarefas_concluidas = request.POST.getlist('tarefas_concluidas')
            for tarefa_id in tarefas_concluidas:
                tarefa = Tarefa.objects.get(id=tarefa_id)
                tarefa.concluida = True
                tarefa.data_conclusao = datetime.now()
                tarefa.save()
                tarefas = Tarefa.objects.filter(user=request.user)
        return redirect('home')

    user = request.user
    tarefas = Tarefa.objects.filter(user=user).order_by(F('concluida').asc(), 'data_criacao')
    return render(request, 'home/index.html', {'tarefas': tarefas})

@login_required
def user_logout(request):  
    logout(request)
    return redirect('login')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Tarefa, id=task_id)
        task.delete()
        return redirect('home')
    else:
        return HttpResponse('Método não permitido.', status=405)
