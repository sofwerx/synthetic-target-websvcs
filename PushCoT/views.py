import os
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from swx.cot import CoT
import json
import urllib

ATAK_IP = os.getenv("ATAK_IP", "192.168.1.160")
ATAK_PORT = int(os.getenv("ATAK_PORT", "4242"))
ATAK_PROTO = os.getenv("ATAK_PROTO", "UDP")

@csrf_exempt
def PushCoT(request):

    req = json.loads(request.body.decode("utf-8"))

    ip_address = ATAK_IP
    if "atak_ip" in req:
      ip_address = req["atak_ip"]

    port = ATAK_PORT
    if "atak_port" in req:
      port = int(req["atak_port"])

    proto = ATAK_PROTO
    if "atak_proto" in req:
      proto = int(req["atak_proto"])

    cot = CoT.CursorOnTarget()
    target = cot.atoms(req)
    if proto == "UDP":
      cot.pushUDP(ip_address, port, target)
    if proto == "TCP":
      cot.pushTCP(ip_address, port, target)
    json_wrapper = {
        "cot_xml": urllib.quote(target)
    }
    resp = HttpResponse(json.dumps(json_wrapper))
    resp.__setitem__("Content-Type", "application/json")
    
    return resp
