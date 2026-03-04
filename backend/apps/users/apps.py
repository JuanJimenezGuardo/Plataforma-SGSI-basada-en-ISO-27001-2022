from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
    
    def ready(self):
        """
        Importar signals cuando la app este lista.
        Esto registra los receivers para User.
        """
        import apps.users.signals
