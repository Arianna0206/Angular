from django.urls import path
from . import views
from django.conf import settings
# from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.incio, name='inicio'),
    path('presupuesto', views.presupuesto, name='presupuesto'),
    path('pets', views.pets, name="pets"),
] 