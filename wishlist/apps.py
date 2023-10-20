from django.apps import AppConfig


class WishlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wishlist'

    def ready(self) -> None:
        import wishlist.signals
        return super().ready()