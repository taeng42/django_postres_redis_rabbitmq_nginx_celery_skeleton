from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods

from .tasks import add, mul

import time
import json

@method_decorator(csrf_exempt, name='dispatch')
def index(request):
    '''
    print("index", flush=True)
    result = add.delay(1, 100)
    result2 = mul.delay(2, 12)
    time.sleep(0.2)
    print(type(result), flush=True)
    print(result, flush=True)
    hashed = 0
    print(hashed, flush=True)

    ret = result
    return HttpResponse(f"{ret.id} {ret.ready()} {ret.get()} {hashed}<br>{result2.id} {result2.ready()} {result2.get()}")
    '''
    result = add.delay(1, 100)
    result2 = mul.delay(2, 12)
    hashed = 0
    ret = result
    time.sleep(0.01)
    print(f"{ret.id} {ret.ready()} {ret.get()} {hashed}<br>{result2.id} {result2.ready()} {result2.get()}", flush=True)

    '''
    print(request.headers)
    print(json.loads(request.body), flush=True)
    resp = HttpResponse("done")
    return resp 
    '''
    #return "Hello"
    return HttpResponse("done", 200)
