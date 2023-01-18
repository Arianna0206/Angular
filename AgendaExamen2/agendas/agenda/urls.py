from django.urls import path
from . import views
from django.conf import settings
# from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pets', views.pets, name="pets"),
    path('pets/crear', views.crear, name="crear"),
    path('pets/editar', views.editar, name="editar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar"),

] 