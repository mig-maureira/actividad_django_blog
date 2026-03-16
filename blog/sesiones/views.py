from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .forms import LoginForm, RegisterForm

# CAMBIO 1: Importamos 'Articulo' en lugar de 'Post'
from posts.models import Articulo


def landing(request):
    # CAMBIO 2: Usamos Articulo y los ordenamos desde el más reciente
    articulos = Articulo.objects.all().order_by("-fecha_publicacion")

    # CAMBIO 3: Pasamos la clave 'articulos' para que coincida con tu nuevo home.html
    return render(request, "home.html", {"articulos": articulos})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect("dashboard_html")
    else:
        form = LoginForm()

    return render(request, "auth/log_in.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado con éxito")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "auth/reg.html", {"form": form})


@login_required
def dashboard(request):
    # CAMBIO 4: Actualizamos también el dashboard para que use Articulo
    articulos = Articulo.objects.all().order_by("-fecha_publicacion")

    # CAMBIO 5: Pasamos la clave 'articulos' al contexto
    return render(request, "auth/dashboard.html", {"articulos": articulos})


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
