from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

import json
#from swx.geopackage-python import geopackage
import urllib

# Create your views here.
def WriteToGeopkg(request):
    req = json.loads(request.body.decode("utf-8"))

    json_wrapper = {
    }
    resp = HttpResponse(json.dumps(json_wrapper))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp