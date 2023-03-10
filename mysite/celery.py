
from __future__ import absolute_import
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


app = Celery("mysite")


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task
def add(x, y):
    return x / y
