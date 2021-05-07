from django.urls import path
from Aplicaciones.Academico.views import CursoListView, eliminar_curso

urlpatterns = [
    path('', CursoListView.as_view(), name='gestion_cursos'),
    path('eliminacionCurso/<int:id>', eliminar_curso)
]
