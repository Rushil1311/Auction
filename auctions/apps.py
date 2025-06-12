from django.apps import AppConfig


class AuctionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # ✅ Fix for warnings
    name = 'auctions'

