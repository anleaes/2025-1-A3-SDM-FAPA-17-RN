from django.urls import path, include
from django.contrib import admin
from .views import (
    AlunoListCreateView,
    AlunoRetrieveUpdateDestroyView,
    ProfessorListCreateView,
    ProfessorRetrieveUpdateDestroyView,
    TurmaListCreateView,
    TurmaRetrieveUpdateDestroyView,
    DisciplinaListCreateView,
    DisciplinaRetrieveUpdateDestroyView,
    NotaListCreateView,
    NotaRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyView.as_view(), name='aluno-detail'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('professores/', ProfessorListCreateView.as_view(), name='professor-list-create'),
    path('professores/<int:pk>/', ProfessorRetrieveUpdateDestroyView.as_view(), name='professor-detail'),
    path('turmas/', TurmaListCreateView.as_view(), name='turma-list-create'),
    path('turmas/<int:pk>/', TurmaRetrieveUpdateDestroyView.as_view(), name='turma-detail'),
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroyView.as_view(), name='disciplina-detail'),
]

