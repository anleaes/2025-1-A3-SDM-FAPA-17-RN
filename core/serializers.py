from rest_framework import serializers
from .models import Aluno
from .models import Professor

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