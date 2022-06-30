from django.conf import settings
from celery import Celery
from celery.result import AsyncResult

brokers = [f'pyamqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{host}//' for host in settings.RABBITMQ_HOSTS]

backend = f'rpc://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}//'

app = Celery('test_app', backend=backend, broker=brokers)
        #broker_transport_options={'confirm_publish': True})

import time

@app.task
def add(x, y):
    print("add!!", flush=True)
    sleep(10)
    return x + y


@app.task
def mul(x, y):
    print("mul!!", flush=True)
    sleep(10)
    return x * y


@app.task(bind=True)
def state(self):
    return self.AsyncResult(self.request.id).state
