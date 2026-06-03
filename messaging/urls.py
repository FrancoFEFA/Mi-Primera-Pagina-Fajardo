from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.BandejaEntradaView.as_view(), name='bandeja'),
    path('enviar/', views.MensajeCreateView.as_view(), name='enviar'),
    path('enviados/', views.mensajes_enviados, name='enviados'),
    path('conversacion/<str:username>/', views.ver_conversacion, name='ver_conversacion'),
]
