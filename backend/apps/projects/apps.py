from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.projects'
    
    def ready(self):
        """
        Importar signals cuando la app este lista.
        Esto registra los receivers para Project, Phase, Task, ProjectUser.
        """
        import apps.projects.signals
