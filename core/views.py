from rest_framework import generics
from .models import (  
    Aluno, 
    Professor,
    Turma,
    Disciplina,
    Frequencia,
    Nota,
    CarrinhoMatricula,
    Perfil,
)
from .serializers import (
    AlunoSerializer,
    ProfessorSerializer,
    TurmaSerializer,
    DisciplinaSerializer,
    NotaSerializer,
    FrequenciaSerializer,
    CarrinhoMatriculaSerializer,
    PerfilSerializer,
)


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

class DisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all().order_by('nome')
    serializer_class = DisciplinaSerializer

class DisciplinaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all().order_by('nome')
    serializer_class = DisciplinaSerializer

class NotaListCreateView(generics.ListCreateAPIView):
    queryset = Nota.objects.all().order_by('data_lancamento')
    serializer_class = NotaSerializer

class NotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all().order_by('data_lancamento')
    serializer_class = NotaSerializer

class FrequenciaListCreateView(generics.ListCreateAPIView):
    queryset = Frequencia.objects.all().order_by('data')
    serializer_class = FrequenciaSerializer

class FrequenciaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Frequencia.objects.all().order_by('data')
    serializer_class = FrequenciaSerializer

class CarrinhoMatriculaListCreateView(generics.ListCreateAPIView):
    queryset = CarrinhoMatricula.objects.all().order_by('-data_criacao')
    serializer_class = CarrinhoMatriculaSerializer

class CarrinhoMatriculaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarrinhoMatricula.objects.all().order_by('-data_criacao')
    serializer_class = CarrinhoMatriculaSerializer

class PerfilListCreateView(generics.ListCreateAPIView):
    queryset = Perfil.objects.all().order_by('nome')
    serializer_class = PerfilSerializer

class PerfilRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all().order_by('nome')
    serializer_class = PerfilSerializer
