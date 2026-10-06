from django.http import JsonResponse
from .models import Avaliacao

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values('id', 'aluno', 'disciplina', 'nota', 'data_criacao', 'status', 'comentario')
    return JsonResponse(list(avaliacoes), safe=False)

def listar_avaliacoes_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status='PENDENTE').values('id','aluno','disciplina','nota','data_criacao','status','comentario')
    return JsonResponse(list(avaliacoes), safe=False)