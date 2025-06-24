from django.urls import path
from .views import AlunoListCreateView
from .views import AlunoRetrieveUpdateDestroyView

urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyView.as_view(), name='aluno-detail'),
]

