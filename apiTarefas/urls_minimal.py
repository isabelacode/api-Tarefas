from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World - Django funcionando!")

urlpatterns = [
    path('hello/', hello_world, name='hello'),
]
