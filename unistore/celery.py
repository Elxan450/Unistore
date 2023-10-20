# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unistore.settings")
app = Celery("unistore")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()



# python -m celery -A unistore worker -l info
# celery -A unistore worker --beat --scheduler django --loglevel=info
