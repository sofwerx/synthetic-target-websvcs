from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
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
    keeper = {lat: req.lat, lon: req.lon, aob: aob}
    # TODO: stuff keeper somewhere
    
    keepers_three = {
        coords:
        [
            {
            lat: 00,
             lon: 00,
             aob: 00 
             },
            {
            lat: 00,
             lon: 00,
             aob: 00 
             },
            {
            lat: 00,
             lon: 00,
             aob: 00 
             }
        ]
    }
    
    # if this is the 3rd point, triangulate & post to map server (or display)
    t = Triangulator.TargetLoc(keepers_three)
    targetLoc = t.locate(request.body.decode("utf-8"))
    
    resp = HttpResponse(json.dumps(targetLoc))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
