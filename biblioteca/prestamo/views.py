from django.shortcuts import render
from .models import Libro, Alumno


# Create your views here.
def index(request):
    lista_libros = Libro.objects.all()
    context = {
        'libros': lista_libros
    }
    return render(request, 'prestamo/index.html', context)


def prestar(request, l_id):
    libro_x = Libro.objects.get(pk=l_id)
    context = {
        'libro': libro_x
    }
    return render(request, 'prestamo/prestamos.html', context)


def prestando(request, l_id):
    libro_x = Libro.objects.get(pk=l_id)
    alumno_nuevo = Alumno.objects.create(
        libro_prestado=libro_x,
        nombre_alumno=request.POST['alumno']
    )
    context = {
        'libro': libro_x
    }
    return render(request, 'prestamo/prestamos.html', context)
