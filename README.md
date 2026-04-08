Blog Django: Guía de Configuración y Uso del ORM

Este repositorio contiene un proyecto base de Django configurado para gestionar publicaciones de blog mediante una relación de modelos Autor-Artículo. Incluye la configuración necesaria para conectar una base de datos PostgreSQL y ejemplos prácticos de uso del ORM.
📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

    Python 3.x

    PostgreSQL

    Un entorno virtual (recomendado)

🛠️ Instalación y Configuración

1. Inicialización del Proyecto

Si estás comenzando desde cero, prepara el entorno y las aplicaciones base:

```Bash
# Crear el proyecto y la aplicación de posts
django-admin startproject blog .
python manage.py startapp posts
```

_.[tip]._
Nota: No olvides registrar posts en la lista INSTALLED_APPS dentro de blog/settings.py.

2. Configuración de la Base de Datos

Para conectar Django con PostgreSQL, instala el adaptador necesario:

```Bash
pip install psycopg2-binary

```

Luego, actualiza el diccionario DATABASES en blog/settings.py con tus credenciales locales:

```Bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_blog_db',         # El nombre de la BD que creaste
        'USER': 'tu_usuario',         # Tu usuario de Postgres
        'PASSWORD': 'tu_password',    # Tu contraseña
        'HOST': 'localhost',          # O la IP donde esté alojada la BD
        'PORT': '5432',               # Puerto por defecto de Postgres
     }
}

```

🏗️ Estructura de Datos (Modelos)

El núcleo de la aplicación reside en posts/models.py, donde definimos una relación One-to-Many (Un autor, muchos artículos).

```Bash
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Relación: Si se elimina el autor, se eliminan sus artículos (CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='articulos')

    def __str__(self):
        return self.titulo
```

🚀 Despliegue de Migraciones

Para impactar los modelos definidos en tu base de datos PostgreSQL, ejecuta los siguientes comandos:

# Prepara los archivos de migración

```Bash
# Generar los archivos de migración
python manage.py makemigrations posts

# Aplicar los cambios a la base de datos
python manage.py migrate

```

💻 Interacción con el ORM (Django Shell)

Puedes probar la lógica de negocio directamente desde la terminal interactiva:

```Bash
python manage.py shell
```

Operaciones de ejemplo:

```Bash

from posts.models import Autor, Articulo

# --- 1. Creación de registros ---
autor_1 = Autor.objects.create(
    nombre="Ada Lovelace",
    correo="ada@ejemplo.com",
    biografia="Pionera de la programación."
)

Articulo.objects.create(
    titulo="Introducción a Django",
    contenido="Django es un framework potente...",
    autor=autor_1
)

# --- 2. Consultas (Queries) ---
# Obtener artículos usando el related_name
articulos_autor = autor_1.articulos.all()

# Filtrado avanzado por atributos del autor
consulta = Articulo.objects.filter(autor__nombre="Ada Lovelace")


```

🛠️ Tecnologías utilizadas

    Framework: Django

    Base de Datos: PostgreSQL

    Lenguaje: Python
