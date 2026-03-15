from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    publicado = models.BooleanField(default=True)
    categoria = models.CharField(max_length=50)

    class Meta:
        db_table = "posts"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo
