# actividad_django_blog

# 1. Levantar un proyecto Django

Por lo que veo en tu archivo, este paso ya lo tienes parcialmente resuelto, ya que cuentas con tu archivo manage.py , la carpeta de configuración blog , y las aplicaciones posts y sesiones.

Si estuvieras partiendo desde cero, los comandos para llegar a este punto serían:

```Bash
django-admin startproject blog .
python manage.py startapp posts
```

(Asegúrate de que la app posts esté agregada en la lista INSTALLED_APPS dentro de tu archivo blog/settings.py ). 2. Levantar una base de datos Postgres con credenciales

# 2. Levantar una base de datos Postgres con credenciales

Antes de conectar Django, necesitas que PostgreSQL esté corriendo en tu sistema o en un contenedor Docker.

    Abre tu gestor de Postgres (como pgAdmin o psql en la terminal).

    Crea una base de datos nueva (ej. mi_blog_db).

    Asegúrate de tener un usuario y contraseña válidos con permisos sobre esa base de datos.

Nota: Para que Django pueda comunicarse con Postgres, necesitas instalar el adaptador de base de datos para Python ejecutando en tu terminal:
Bash

```Bash
pip install psycopg2-binary
```

# 3. Configurar el acceso en settings.py

Debes abrir el archivo blog/settings.py y buscar la variable DATABASES. Vamos a reemplazar la configuración actual de SQLite por las credenciales de tu nueva base de datos Postgres:
Python

# blog/settings.py

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

# 4. Crear los modelos de datos en models.py

Aquí definiremos las clases Autor y Articulo, estableciendo una relación de "Uno a Muchos" (un autor puede tener muchos artículos).
Python

# posts/models.py

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

# 5. Hacer la migración de datos

En tu terminal, ejecuta:

# Prepara los archivos de migración

```Bash
python manage.py makemigrations posts
```

# Aplica los cambios en la base de datos Postgres

```Bash
python manage.py migrate
```

# 6. Crear entradas y realizar una consulta ORM

Para interactuar con la base de datos usando el ORM de Django, abriremos la consola interactiva (shell):

```Bash
python manage.py shell
```

Una vez dentro de la consola de Python, ejecuta los siguientes comandos para crear registros y consultarlos:
Python

# Importar los modelos

```Bash
from posts.models import Autor, Articulo

# 1. CREAR NUEVAS ENTRADAS

# Crear un Autor

autor1 = Autor.objects.create(nombre="Ada Lovelace", correo="ada@ejemplo.com", biografia="Pionera de la programación.")

# Crear un Artículo vinculado a ese Autor

articulo1 = Articulo.objects.create(titulo="Introducción a Django", contenido="Django es un framework...", autor=autor1)

# 2. REALIZAR UNA CONSULTA ORM

# Consultar todos los artículos creados por el autor1 usando la relación inversa (related_name)

articulos_de_ada = autor1.articulos.all()
print(articulos_de_ada)

# Otra forma de consultar filtrando directamente en el modelo Articulo:

consulta_filtrada = Articulo.objects.filter(autor\_\_nombre="Ada Lovelace")
print(consulta_filtrada)
```

Para salir de la consola, simplemente escribe exit().
