from rest_framework import serializers
from .models import Aluno
from .models import Professor
from .models import Turma

class AlunoSerializer(serializers.ModelSerializer):
    professor = serializers.StringRelatedField()

    class Meta:
        model = Aluno
        fields = '__all__'
        read_only_fields = ('id',)  

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        read_only_fields = ('id',)

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'
        read_only_fields = ['id']


#name = 'core'
#version = 'v1'
# This file contains serializers for the core application models.