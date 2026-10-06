from .views import listar_disciplinas
from django.urls import path

urlpatterns = [
    path('disciplinas/', listar_disciplinas),
]