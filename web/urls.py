from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eliminar_registro/<int:pk>', views.registro_eliminar, name='registro_eliminar'),
    path('agregar_registro/', views.registro_agregar, name='registro_agregar'),
    path('registro/<int:pk>', views.registro_editar, name='registro_editar'),
]