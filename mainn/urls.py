from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Socios
    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/crear/', views.crear_socio, name='crear_socio'),
    path('socios/<int:socio_id>/avatar/', views.upload_avatar, name='upload_avatar'),
    path('socios/<int:socio_id>/avatar/eliminar/', views.eliminar_avatar, name='eliminar_avatar'),

    # Entrenadores
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/crear/', views.crear_entrenador, name='crear_entrenador'),

    # Rutinas
    path('rutinas/', views.lista_rutinas, name='lista_rutinas'),
    path('rutinas/crear/', views.crear_rutina, name='crear_rutina'),

    # Asistencias
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
]