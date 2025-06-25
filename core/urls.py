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
    FrequenciaListCreateView,
    FrequenciaRetrieveUpdateDestroyView,
    CarrinhoMatriculaListCreateView,
    CarrinhoMatriculaRetrieveUpdateDestroyView,
    PerfilListCreateView,
    PerfilRetrieveUpdateDestroyView,
    UsuarioListCreateView,
    UsuarioRetrieveUpdateDestroyView,
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
    path('notas/', NotaListCreateView.as_view(), name='nota-list-create'),
    path('notas/<int:pk>/', NotaRetrieveUpdateDestroyView.as_view(), name='nota-detail'),
    path('frequencias/', FrequenciaListCreateView.as_view(), name='frequencia-list-create'),
    path('frequencias/<int:pk>/', FrequenciaRetrieveUpdateDestroyView.as_view(), name='frequencia-detail'),
    path('carrinhos/', CarrinhoMatriculaListCreateView.as_view(), name='carrinho-list-create'),
    path('carrinhos/<int:pk>/', CarrinhoMatriculaRetrieveUpdateDestroyView.as_view(), name='carrinho-detail'),
    path('perfis/', PerfilListCreateView.as_view(), name='perfil-list-create'),
    path('perfis/<int:pk>/', PerfilRetrieveUpdateDestroyView.as_view(), name='perfil-detail'),
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
]

