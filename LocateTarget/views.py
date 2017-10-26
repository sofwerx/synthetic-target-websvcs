from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import json

from swx.triangulator import Triangulator

@csrf_exempt
def LocateTarget(request):
    
    t = Triangulator.TargetLoc()
    [hasIntersect, (lat, lon)] = t.locate(request.body.decode("utf-8"))
    
    targetLoc = json.dumps({"hasIntersect": hasIntersect, "targetLoc": {"lat": lat, "lon": lon }})
    
    resp = HttpResponse(targetLoc)
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
