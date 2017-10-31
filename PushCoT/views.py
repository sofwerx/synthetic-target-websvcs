from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from swx.cot import PushCoT
import json

@csrf_exempt
def PushCoT(request):

    cot = PushCoT.CursorOnTarget()
    target = cot.atoms(json.loads(request.body.decode("utf-8")))
    cot.pushUDP(target)
    resp = HttpResponse(target)
    resp.__setitem__("Content-Type", "application/xml")
    
    return resp
