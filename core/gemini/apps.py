from django.apps import AppConfig


class GeminiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.gemini'
    
    def ready(self):
        import core.gemini.signals
