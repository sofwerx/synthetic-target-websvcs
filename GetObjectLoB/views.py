from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from swx.object_lob import ObjectLoB
import json

@csrf_exempt
def GetObjectLoB(request):
    
    person = ObjectLoB.personLoB(request.body.decode("utf-8"))
    resp = HttpResponse(json.dumps(person))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
