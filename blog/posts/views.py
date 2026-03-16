from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Articulo
from .forms import ArticuloForm


@login_required
def crear_articulo(request):

    autor, created = Autor.objects.get_or_create(
        usuario=request.user,
        defaults={"nombre": request.user.username, "correo": request.user.email},
    )

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")

        Articulo.objects.create(titulo=titulo, contenido=contenido, autor=autor)

        return redirect("dashboard_html")

    return render(request, "articulos/crear_articulos.html")


@login_required
def editar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)

    # impedir editar artículos de otros autores
    if articulo.autor.usuario != request.user:
        return redirect("home")

    form = ArticuloForm(request.POST or None, instance=articulo)

    if form.is_valid():
        form.save()
        return redirect("detalle_articulo", articulo_id=articulo.id)

    return render(
        request, "articulos/upd_articulos.html", {"form": form, "articulo": articulo}
    )


@login_required
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    es_editor = request.user.groups.filter(name="editor").exists()
    es_autor = articulo.autor.usuario == request.user

    if not (es_autor or es_editor):
        return redirect("home")

    if request.method == "POST":
        articulo.delete()
        return redirect("home")

    return render(request, "articulos/del_articulos.html", {"articulo": articulo})


def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    # Traemos por ejemplo los últimos 5 artículos
    articulos_recientes = Articulo.objects.all().order_by("-fecha_publicacion")[:5]

    return render(
        request,
        "articulos/single.html",
        {"articulo": articulo, "articulos_recientes": articulos_recientes},
    )
