# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso

# Create your views here.


def home(request):
    cursosListados = Curso.objects.all()
    # cursosListados = Curso.objects.all()[:5]
    # cursosListados = Curso.objects.all()[4:9]
    # cursosListados = Curso.objects.all().order_by('nombre')
    # cursosListados = Curso.objects.all().order_by('-nombre')
    # cursosListados = Curso.objects.all().order_by('nombre', 'creditos')
    # cursosListados = Curso.objects.filter(nombre='Historia', creditos=5)
    # cursosListados = Curso.objects.filter(creditos__lte=4)
    # cursosListados = Curso.objects.filter(nombre__startswith='Q')
    # cursosListados = Curso.objects.filter(nombre__contains='g')

    # return HttpResponse("<h1>Hola Mundo!</h1>")
    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': cursosListados
    }
    # return render(request, "gestionCursos.html", {"cursos": cursosListados})
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
