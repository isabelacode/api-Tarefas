from rest_framework.serializers import ModelSerializer
from tarefas.models import Tarefa

class TarefaSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo']

class TarefaDetalhadaSerializer(ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'user', 'titulo', 'descricao', 'data_criacao', 'data_conclusao', 'concluida']
