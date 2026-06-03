from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),

    # Socios
    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/crear/', views.crear_socio, name='crear_socio'),
    path('socios/<int:socio_id>/', views.detalle_socio, name='detalle_socio'),
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

    # Rutinas (lista como CBV, el resto como FBV)
    path('rutinas/', views.RutinaListView.as_view(), name='lista_rutinas'),
    path('rutinas/crear/', views.crear_rutina, name='crear_rutina'),
    path('rutinas/<int:rutina_id>/editar/', views.editar_rutina, name='editar_rutina'),
    path('rutinas/<int:rutina_id>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),

    # Asistencias
    path('asistencias/', views.lista_asistencias, name='lista_asistencias'),
    path('asistencias/crear/', views.crear_asistencia, name='crear_asistencia'),
    path('asistencias/checkin/<int:socio_id>/', views.checkin_rapido, name='checkin_rapido'),
    path('asistencias/<int:asistencia_id>/eliminar/', views.eliminar_asistencia, name='eliminar_asistencia'),
]
