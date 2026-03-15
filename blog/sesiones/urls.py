from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="home"),
    path("auth/log_in/", views.login_view, name="login"),
    path("auth/reg/", views.register_view, name="register"),
    path("auth/log_out/", views.logout_view, name="logout"),
    path("auth/dashboard/", views.dashboard, name="dashboard_html"),
]
