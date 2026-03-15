from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


@login_required
def crear_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")

        Post.objects.create(titulo=titulo, contenido=contenido, autor=request.user)

        return redirect("dashboard_html")

    return render(request, "posts/crear_post.html")


@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # impedir editar posts de otros usuarios
    if post.autor != request.user:
        return redirect("home")

    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect("detalle_post", post_id=post.id)

    return render(request, "posts/upd_post.html", {"form": form, "post": post})


@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    es_editor = request.user.groups.filter(name="editor").exists()
    es_autor = post.autor == request.user

    # Solo puede borrar si es autor o editor
    if not (es_autor or es_editor):
        return redirect("home")

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "posts/del_post.html", {"post": post})


def detalle_post(request, post_id):
    # 1. Buscamos el post principal
    post = get_object_or_404(Post, id=post_id)

    # 2. Traemos otros 5 posts (excluyendo el actual)
    recent_posts = Post.objects.exclude(id=post.id).order_by("-fecha_creacion")[:5]

    return render(
        request,
        "posts/single.html",
        {
            "post": post,
            "recent_posts": recent_posts,
        },
    )
