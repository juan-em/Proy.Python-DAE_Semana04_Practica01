from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre_libro = models.CharField(max_length=200)


class Alumno(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    nombre_alumno = models.CharField(max_length=200)