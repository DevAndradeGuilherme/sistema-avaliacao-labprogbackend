from django.http import JsonResponse
from django.db.models import Avg, Count

from .models import Avaliacao

def listar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().values('id', 'aluno', 'disciplina', 'nota', 'data_criacao', 'status', 'comentario')
    return JsonResponse(list(avaliacoes), safe=False)

def listar_avaliacoes_pendentes(request):
    avaliacoes = Avaliacao.objects.filter(status='PENDENTE').values('id','aluno','disciplina','nota','data_criacao','status','comentario')
    return JsonResponse(list(avaliacoes), safe=False)

def resumo_avaliacoes(request):
    resumo = (Avaliacao.objects.filter(status='RESPONDIDA').values('disciplina', 'disciplina__nome').annotate(media_notas=Avg('nota'), total_avaliacoes=Count('id')))
    return JsonResponse(list(resumo), safe=False)