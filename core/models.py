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
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    formacao = models.CharField(max_length=100)
    area_atuacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    periodo = models.CharField(
        max_length=20,
        choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')],
        default='Manhã'
    )
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='turmas')

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.periodo}"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='disciplinas')
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return self.nome

class Nota(models.Model):
    valor = models.FloatField()
    data_lancamento = models.DateField()
    observacao = models.CharField(max_length=255, blank=True)  # novo atributo
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='notas')
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, related_name='notas')


    def __str__(self):
        return f"{self.valor} - {self.aluno.nome}"

class Frequencia(models.Model):
    STATUS_CHOICES = [
        ('Presente', 'Presente'),
        ('Faltou', 'Faltou'),
        ('Justificada', 'Justificada'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Presente')
    data = models.DateField()
    justificativa = models.TextField(blank=True)
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='frequencias')

    def __str__(self):
        return f"{self.aluno.nome} - {self.status} em {self.data}"

class CarrinhoMatricula(models.Model):
    status = models.CharField(max_length=30)
    data_criacao = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE, related_name='carrinhos')

    def __str__(self):
        return f"Carrinho de {self.aluno.nome} - Status: {self.status}"

class Perfil(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.login
