from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from alunos.models import Aluno
from disciplinas.models import Disciplina


class Avaliacao(models.Model):

    status_choices = [
        ('PENDENTE', 'pendente'),
        ('RESPONDIDA', 'respondida')
    ]

    nota = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)    
        ]
    )
    comentario = models.TextField(max_length=500)
    status = models.CharField(max_length=16,choices=status_choices, default='PENDENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

def __str__(self):
    return f"{self.nota} - {self.comentario}"   