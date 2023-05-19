from rest_framework.response import Response
from .models import *

def on_message_sensor1(client, userdata, msg):
    Sensor1.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor1.objects.count() > 200:
        Sensor1.objects.all().first().delete()

def on_message_sensor2(client, userdata, msg):
    Sensor2.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor2.objects.count() > 200:
        Sensor2.objects.all().first().delete()

def on_message_sensor3(client, userdata, msg):
    Sensor3.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor3.objects.count() > 200:
        Sensor3.objects.all().first().delete()

def on_message_aktuator1(msg):
    Aktuator1.objects.create(value=str(msg))
    if Aktuator1.objects.count() > 200:
        Aktuator1.objects.all().first().delete()
