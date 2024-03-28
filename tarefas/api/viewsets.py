from rest_framework import viewsets, status
from tarefas.models import Tarefa
from .serializers import TarefaSerializer, TarefaDetalhadaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

class TarefasViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.order_by('data_criacao')
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action== 'retrieve':
            return TarefaDetalhadaSerializer
        return TarefaSerializer
    
    @action(detail=True, methods=['get'])
    def concluida(self, request, pk=None):
        try:
            tarefa = self.get_object()
        except Tarefa.DoesNotExist:
            return Response({"error": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        tarefa.concluida = True
        tarefa.save()
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data)