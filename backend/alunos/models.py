from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ra = models.CharField(max_length=128, unique=True)
    curso = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome