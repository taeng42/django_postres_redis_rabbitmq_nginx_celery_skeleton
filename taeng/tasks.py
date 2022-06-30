from django.conf import settings
from celery import Celery
from celery.result import AsyncResult

brokers = [f'amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{host}//' for host in settings.RABBITMQ_HOSTS]

broker = f'rpc://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}//'

app = Celery('taeng', backend=broker, broker=brokers,
        broker_transport_options={'confirm_publish': True})

import time

@app.task
def add(x, y):
    print("add?", flush=True)
    sleep(10)
    return x + y
