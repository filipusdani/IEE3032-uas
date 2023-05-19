from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

import paho.mqtt.client as mqtt
from .mqtt import *
from .ml import *

def home(req):    
    return render(req, "index.html")

def api(req):
    np_chart = (list((Aktuator1.objects.all())))[190:]
    a1_chart_value = ([o.value for o in np_chart])
    a1_chart_labels = ([str(o.date_created)[11:19] for o in np_chart])
    data = {
        "Sensor1": serialize("json", list(reversed(Sensor1.objects.all()))),
        "Sensor2": serialize("json", list(reversed(Sensor2.objects.all()))),
        "Sensor3": serialize("json", list(reversed(Sensor3.objects.all()))),
        "Aktuator1": list(reversed(Aktuator1.objects.all()))[1].value,
        "a1_chart_value": a1_chart_value,
        "a1_chart_labels": a1_chart_labels,
    }    
    hitung_ml()
    return JsonResponse(data)

def hitung_ml():
    aSensor1 = (list(reversed(Sensor1.objects.all())))[0].value
    aSensor2 = (list(reversed(Sensor2.objects.all())))[0].value
    aSensor3 = (list(reversed(Sensor3.objects.all())))[0].value
    aktuator1 = hitung_aktuator1(aSensor1,aSensor2,aSensor3)
    on_message_aktuator1(aktuator1)

client = mqtt.Client("prauas")
client.message_callback_add('uas/sensor1', on_message_sensor1)
client.message_callback_add('uas/sensor2', on_message_sensor2)
client.message_callback_add('uas/sensor3', on_message_sensor3)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('uas/#')