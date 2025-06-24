from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer


class AlunoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer
