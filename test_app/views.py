from django.shortcuts import render
from django.http import HttpResponse

from .tasks import add, mul

import time


def index(request):
    print("index", flush=True)
    result = add.delay(1, 100)
    result2 = mul.delay(2, 12)
    time.sleep(0.002)
    print(type(result), flush=True)
    print(result, flush=True)
    hashed = 0
    print(hashed, flush=True)

    ret = result
    return HttpResponse(f"{ret.id} {ret.ready()} {ret.get()} {hashed}<br>{result2.id} {result2.ready()} {result2.get()}")
