from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Perfil extendido del usuario con información adicional."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, verbose_name='Biografía')
    avatar = models.ImageField(
        upload_to='perfiles/',
        blank=True,
        null=True,
        verbose_name='Avatar',
    )
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')
    ciudad = models.CharField(max_length=80, blank=True, verbose_name='Ciudad')

    def __str__(self):
        return f"Perfil de {self.user.username}"

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
