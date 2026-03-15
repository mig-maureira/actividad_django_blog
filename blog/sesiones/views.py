from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .forms import LoginForm, RegisterForm
from posts.models import Post


def landing(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


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
    posts = Post.objects.all()
    return render(request, "auth/dashboard.html", {"posts": posts})


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
