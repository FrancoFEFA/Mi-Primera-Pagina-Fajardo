from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.ProfileUpdateView.as_view(), name='editar_perfil'),
    path('perfil/<str:username>/', views.perfil_publico, name='perfil_publico'),
]
