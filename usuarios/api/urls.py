from django.urls import path
from .. import views
from ..views import user_logout, delete_task

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'), 
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    
]

