# from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "gestionCursos.html", {"cursos": cursosListados})
