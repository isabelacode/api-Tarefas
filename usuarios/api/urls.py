from django.urls import path
from .. import views
from ..views import user_logout, delete_task
from .viewsets import (
    register_user, 
    user_profile, 
    login_user, 
    password_reset_request, 
    password_reset_confirm
)
from .test_views import test_endpoint
from .simple_test import simple_test

urlpatterns = [
    path('api/simple/', simple_test, name='simple_test'),
    
    path('api/test/', test_endpoint, name='test_endpoint'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'), 
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    
    path('api/register/', register_user, name='api_register'),
    path('api/login/', login_user, name='api_login'),
    path('api/profile/', user_profile, name='api_profile'),
    path('api/password-reset/', password_reset_request, name='api_password_reset'),
    path('api/password-reset-confirm/<str:uidb64>/<str:token>/', password_reset_confirm, name='api_password_reset_confirm'),
]

