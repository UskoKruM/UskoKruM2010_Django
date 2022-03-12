from django.urls import path
from Aplicaciones.Academico.views import CursoListView, registrar_curso, eliminar_curso, edicion_curso, editar_curso, contacto

urlpatterns = [
    path('', CursoListView.as_view(), name='gestion_cursos'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso),
    path('contacto/', contacto),
]
