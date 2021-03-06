# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Curso

# Create your views here.


def home(request):
    cursos_listados = Curso.objects.all()
    # cursos_listados = Curso.objects.all()[:5]
    # cursos_listados = Curso.objects.all()[4:9]
    # cursos_listados = Curso.objects.all().order_by('nombre')
    # cursos_listados = Curso.objects.all().order_by('-nombre')
    # cursos_listados = Curso.objects.all().order_by('nombre', 'creditos')
    # cursos_listados = Curso.objects.filter(nombre='Historia', creditos=5)
    # cursos_listados = Curso.objects.filter(creditos__lte=4)
    # cursos_listados = Curso.objects.filter(nombre__startswith='Q')
    # cursos_listados = Curso.objects.filter(nombre__contains='g')

    # return HttpResponse("<h1>Hola Mundo!</h1>")
    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': cursos_listados
    }
    # return render(request, "gestionCursos.html", {"cursos": cursos_listados})
    return render(request, "gestionCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestión de Cursos'
        # print(context)
        return context


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')
