from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from swx.cot import CoT
import json
import urllib

@csrf_exempt
def PushCoT(request):

    cot = CoT.CursorOnTarget()
    target = cot.atoms(json.loads(request.body.decode("utf-8")))
    cot.pushUDP(target)
    json_wrapper = {
        "cot_xml": urllib.quote(target)
    }
    resp = HttpResponse(json.dumps(json_wrapper))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
