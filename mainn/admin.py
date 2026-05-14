from django.contrib import admin
from .models import Socio, Entrenador, Rutina, Asistencia

# Registrar todos los modelos en el panel de administración
admin.site.register([Socio, Entrenador, Rutina, Asistencia])
