from .views import listar_avaliacoes, listar_avaliacoes_pendentes, resumo_avaliacoes
from django.urls import path

urlpatterns = [
    path('avaliacoes/', listar_avaliacoes),
    path('avaliacoes/pendentes/', listar_avaliacoes_pendentes),
    path('avaliacoes/resumo/', resumo_avaliacoes),
]