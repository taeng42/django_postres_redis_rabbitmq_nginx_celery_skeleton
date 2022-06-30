from django.shortcuts import render
from django.http import HttpResponse

from .tasks import mul
from taeng.tasks import add

def index(request):
    print("index", flush=True)
    result = add.delay(2, 6)
    ret = result

    return HttpResponse(f"{ret}:\t{ret.id} {ret.status} {ret.ready()}")
