
from django.apps import AppConfig
# from . import signals  # Relative import (This should work)


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        import backend.signals  # Import the signals to make them active

