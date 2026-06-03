from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import User
        from .models import Profile

        def crear_perfil(sender, instance, created, **kwargs):
            if created:
                Profile.objects.get_or_create(user=instance)

        post_save.connect(crear_perfil, sender=User)
