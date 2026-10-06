from django.http import JsonResponse
from .models import Disciplina
def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all().values('id', 'nome', 'codigo', 'professor', 'periodo')
    return JsonResponse(list(disciplinas), safe=False)