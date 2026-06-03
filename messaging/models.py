from django.db import models
from django.contrib.auth.models import User


class Mensaje(models.Model):
    """Mensaje privado entre dos usuarios del sistema."""

    emisor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mensajes_enviados',
    )
    receptor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mensajes_recibidos',
    )
    contenido = models.TextField(verbose_name='Mensaje')
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.emisor.username} para {self.receptor.username} ({self.fecha_envio:%d/%m/%Y %H:%M})"

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['-fecha_envio']
