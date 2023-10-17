import os

from celery import Celery

# Make celery access to settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Set how celery access to celery config defined in settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Make celery aware of project tasks
app.autodiscover_tasks()
