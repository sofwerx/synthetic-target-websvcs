from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import json

from swx.triangulator import Triangulator

import logging

logger = logging.getLogger("django")


@csrf_exempt
def LocateTarget(request):
    
    t = Triangulator.TargetLoc()
    logger.info("LocateTarget body=%s",request.body)
    targetLoc = t.locate(json.loads(request.body.decode("utf-8")))
    resp = HttpResponse(json.dumps(targetLoc))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
