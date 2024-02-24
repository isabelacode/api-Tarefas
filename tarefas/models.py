from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Tarefas de {self.user.username}'

