from django.urls import include, path
from rest_framework import routers
from .viewsets import TarefasViewSet
from .. import views

app_name = 'tarefas'
router = routers.DefaultRouter()
router.register(r'tarefas', TarefasViewSet, basename='Tarefas')

urlpatterns = [
    path('', include(router.urls)),
]

