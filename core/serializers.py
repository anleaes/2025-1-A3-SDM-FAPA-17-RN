from rest_framework import serializers
from .models import Aluno, Professor, Turma, Disciplina, Nota, Frequencia


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        read_only_fields = ('id',)  

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ('id',)

class NotaSerializer(serializers.ModelSerializer):
    aluno = serializers.StringRelatedField()

    class Meta:
        model = Nota
        fields = '__all__'
        read_only_fields = ('id',)

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        read_only_fields = ['id']

class DisciplinaSerializer(serializers.ModelSerializer):
    professor = serializers.StringRelatedField()
    turma = serializers.StringRelatedField()

    class Meta:
        model = Disciplina
        fields = '__all__'
        read_only_fields = ('id',)



