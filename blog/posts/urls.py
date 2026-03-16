from django.urls import path
from . import views

# urlpatterns = [
#     path("posts/crear_post", views.crear_post, name="crear_post"),
#     path("posts/del_post/<int:post_id>/", views.eliminar_post, name="del_post"),
#     path("posts/upd_post/<int:post_id>/", views.editar_post, name="upd_post"),
#     path("posts/single/<int:post_id>/", views.detalle_post, name="detalle_post"),
# ]
urlpatterns = [
    path("articulos/crear/", views.crear_articulo, name="crear_articulo"),
    path(
        "articulos/<int:articulo_id>/editar/",
        views.editar_articulo,
        name="editar_articulo",
    ),
    path(
        "articulos/<int:articulo_id>/eliminar/",
        views.eliminar_articulo,
        name="eliminar_articulo",
    ),
    path(
        "articulos/<int:articulo_id>/", views.detalle_articulo, name="detalle_articulo"
    ),
]
