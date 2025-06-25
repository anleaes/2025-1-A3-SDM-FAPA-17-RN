from rest_framework import generics
from .models import Aluno, Professor, Turma, Disciplina
from .serializers import AlunoSerializer, ProfessorSerializer, TurmaSerializer


class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer


class AlunoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer

class ProfessorListCreateView(generics.ListCreateAPIView):
    queryset = Professor.objects.all().order_by('nome')
    serializer_class = ProfessorSerializer

class ProfessorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all().order_by('nome')
    serializer_class = ProfessorSerializer

class TurmaListCreateView(generics.ListCreateAPIView):
    queryset = Turma.objects.all().order_by('ano', 'nome')
    serializer_class = TurmaSerializer

class TurmaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turma.objects.all().order_by('ano', 'nome')
    serializer_class = TurmaSerializer
