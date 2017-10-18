from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import urllib2
import json

###########
# Distributed Telemetry Acquisition
###########
@csrf_exempt
def DTA(request):
    bod = request.body.decode("utf-8")
    # request is JSON: lat, lon, compass, image (base64 enc), camera fov (in degrees)
    req = json.loads(bod)
    
    # call OblectLoB, persist result
    aob = ObjectLoB.PersonLoB(req)
    # persist aob + input json (- image data)

    # if this is the 3rd point, triangulate & post to map server (or display)
    
    resp = HttpResponse(json.dumps(aob))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
