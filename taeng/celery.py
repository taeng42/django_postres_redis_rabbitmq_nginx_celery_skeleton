from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.result import AsyncResult

#brokers = [f'amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{host}//' for host in settings.RABBITMQ_HOSTS]
#app = Celery('taeng', broker=brokers,
        #broker_transport_options={'confirm_publish': True})

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taeng.settings")
app = Celery('taeng')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("request: {0!r}".format(self.request), flush=True)
