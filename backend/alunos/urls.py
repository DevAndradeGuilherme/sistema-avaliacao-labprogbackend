from .views import listar_alunos
from django.urls import path

urlpatterns = [
    path('alunos/', listar_alunos),
]