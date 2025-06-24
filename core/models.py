from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.ano}"

