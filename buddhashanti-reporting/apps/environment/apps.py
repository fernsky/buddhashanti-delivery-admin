from django.apps import AppConfig


class EnvironmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.environment'
    verbose_name = 'Environment'
