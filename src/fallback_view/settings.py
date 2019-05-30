from django.conf import settings

FALLBACK_VIEW_PATH = getattr(settings, "FALLBACK_VIEW", None)


