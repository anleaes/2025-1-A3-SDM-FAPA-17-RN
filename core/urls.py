from django.urls import path, include
from django.contrib import admin
from .views import AlunoListCreateView, AlunoRetrieveUpdateDestroyView, ProfessorListCreateView, ProfessorListCreateView

urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyView.as_view(), name='aluno-detail'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('professores/', ProfessorListCreateView.as_view(), name='professor-list-create'),
]

