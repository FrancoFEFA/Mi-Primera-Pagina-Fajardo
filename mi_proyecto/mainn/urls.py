from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Aquí irán tus rutas, por ejemplo:
    # path('', views.inicio, name='inicio'),
]