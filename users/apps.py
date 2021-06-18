from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'Autorização'
    
    def ready(self) -> None:
        from .utils import start_cron
        start_cron()
        return super().ready()
