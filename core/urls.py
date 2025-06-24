from django.urls import path, include
from django.contrib import admin
from .views import AlunoListCreateView
from .views import AlunoRetrieveUpdateDestroyView

urlpatterns = [
    path('alunos/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyView.as_view(), name='aluno-detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

