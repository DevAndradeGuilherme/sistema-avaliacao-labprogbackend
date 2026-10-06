from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

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
        ],
        null = True,
        blank = True
    )
    comentario = models.TextField(max_length=500, blank = True)
    status = models.CharField(max_length=16,choices=status_choices, default='PENDENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)
    aluno = models.ForeignKey(Aluno,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)

    def clean(self):
        if self.status == 'RESPONDIDA':
            if self.nota is None:
                raise ValidationError({
                    'nota': 'A nota é obrigatória quando a avaliação estiver respondida.'
                })

            if not self.comentario:
                raise ValidationError({
                    'comentario': 'O comentário é obrigatório quando a avaliação estiver respondida.'
                })

    def __str__(self):
        return f"{self.nota} - {self.disciplina} - {self.aluno}"   