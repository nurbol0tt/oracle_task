from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.school"

    def ready(self):
        import apps.school.signals
