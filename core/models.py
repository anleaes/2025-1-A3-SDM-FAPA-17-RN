from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

