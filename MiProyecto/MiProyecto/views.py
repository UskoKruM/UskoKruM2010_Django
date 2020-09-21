from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista: 
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento.
	return HttpResponse("Bienvenido o bienvenida a este curso de Django. =)")

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento.
	return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. ;)</p>")

def categoriaEdad(request, edad):
	if edad >= 18:
		if edad >= 60:
			categoria = "Tercera edad"
		else:
			categoria = "Adultez"
	else:
		if edad < 10:
			categoria = "Infancia"
		else:
			categoria = "Adolescencia"
	resultado = "<h1>Categoría de la edad: %s</h1>" %categoria
	return HttpResponse(resultado)

def obtenerMomentoActual(request):
	# respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
	respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
	return HttpResponse(respuesta)
	
def contenidoHTML(request, nombre, edad):
	contenido =  """
	<html>
	<body>
	<p>Nombre: %s / Edad: %s</p>
	</body>
	</html>
	""" % (nombre, edad)
	return HttpResponse(contenido)

def miPrimeraPlantilla(request):
	# Abrimos el documento que contiene a la plantilla:
	plantillaExterna = open("C:/MiProyecto/MiProyecto/plantillas/miPrimeraPlantilla.html")
	# Cargar el documento en una variable de tipo 'Template':
	template = Template(plantillaExterna.read())
	# Cerrar el documento externo que hemos abierto:
	plantillaExterna.close()
	# Crear un contexto:
	contexto = Context()
	# Renderizar el documento:
	documento = template.render(contexto)
	return HttpResponse(documento)

def plantillaParametros(request):
	"""
	Este 
	es 
	un 
	comentario multilínea.
	"""
	nombre = "UskoKruM2010"
	fechaActual = datetime.datetime.now()
	lenguajes = ["Python", "Ruby", "JavaScript", "Java", "C#", "Kotlin"]
	# Abrimos el documento que contiene a la plantilla:
	plantillaExterna = open("C:/MiProyecto/MiProyecto/plantillas/plantillaParametros.html")
	# Cargar el documento en una variable de tipo 'Template':
	template = Template(plantillaExterna.read())
	# Cerrar el documento externo que hemos abierto:
	plantillaExterna.close()
	# Crear un contexto:
	contexto = Context({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
	# Renderizar el documento:
	documento = template.render(contexto)
	return HttpResponse(documento)

def plantillaCargador(request):
	nombre = "UskoKruM2010"
	fechaActual = datetime.datetime.now()
	lenguajes = ["Python", "Ruby", "JavaScript", "PHP", "Java", "C#", "Kotlin"]
	# Especificando la carpeta donde se encuentran las plantilla y creamos una variable que la almacena:
	plantillaExterna = get_template('plantillaParametros.html')
	# Renderizar el documento:
	documento = plantillaExterna.render({"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})
	return HttpResponse(documento)

def plantillaShortcut(request):
	nombre = "UskoKruM2010"
	fechaActual = datetime.datetime.now()
	lenguajes = ["Python", "Ruby", "JavaScript", "C++", "PHP", "Java", "C#", "Kotlin"]

	return render(request, 'plantillaParametros.html', {"nombreCanal": nombre, "fechaActual": fechaActual, "lenguajes": lenguajes})

def plantillaHija1(request):
	return render(request, "plantillaHija_1.html", {})

def plantillaHija2(request):
	return render(request, "plantillaHija_2.html", {})	