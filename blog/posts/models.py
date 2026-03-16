from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="autor")
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Relación: Si se elimina el autor, se eliminan sus artículos (CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="articulos")

    def __str__(self):
        return self.titulo
