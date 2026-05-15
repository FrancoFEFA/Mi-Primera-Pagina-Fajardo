from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Socios
    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/crear/', views.crear_socio, name='crear_socio'),
    path('socios/<int:socio_id>/avatar/', views.upload_avatar, name='upload_avatar'),
    path('socios/<int:socio_id>/avatar/eliminar/', views.eliminar_avatar, name='eliminar_avatar'),
    path('socios/<int:socio_id>/editar/', views.editar_socio, name='editar_socio'),
    path('socios/<int:socio_id>/eliminar/', views.eliminar_socio, name='eliminar_socio'),

    # Entrenadores
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('entrenadores/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenadores/<int:entrenador_id>/editar/', views.editar_entrenador, name='editar_entrenador'),
    path('entrenadores/<int:entrenador_id>/foto/', views.upload_foto_entrenador, name='upload_foto_entrenador'),
    path('entrenadores/<int:entrenador_id>/foto/eliminar/', views.eliminar_foto_entrenador, name='eliminar_foto_entrenador'),
    path('entrenadores/<int:entrenador_id>/eliminar/', views.eliminar_entrenador, name='eliminar_entrenador'),

    # Rutinas
    path('rutinas/', views.lista_rutinas, name='lista_rutinas'),
    path('rutinas/crear/', views.crear_rutina, name='crear_rutina'),
    path('rutinas/<int:rutina_id>/editar/', views.editar_rutina, name='editar_rutina'),
    path('rutinas/<int:rutina_id>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),

    # Asistencias
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
]