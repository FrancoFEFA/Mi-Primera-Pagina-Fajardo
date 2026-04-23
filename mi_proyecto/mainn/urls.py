from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('personas/', views.lista_personas, name='lista_personas'),
    path('personas/crear/', views.crear_persona, name='crear_persona'),
    # Aquí irán tus rutas, por ejemplo:
    # path('', views.inicio, name='inicio'),
]