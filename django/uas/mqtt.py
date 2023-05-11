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

def on_message_sensor4(client, userdata, msg):
    Sensor4.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor4.objects.count() > 200:
        Sensor4.objects.all().first().delete()

def on_message_sensor5(client, userdata, msg):
    Sensor5.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor5.objects.count() > 200:
        Sensor5.objects.all().first().delete()

def on_message_sensor6(client, userdata, msg):
    Sensor6.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor6.objects.count() > 200:
        Sensor6.objects.all().first().delete()

def on_message_sensor7(client, userdata, msg):
    Sensor7.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor7.objects.count() > 200:
        Sensor7.objects.all().first().delete()

def on_message_sensor8(client, userdata, msg):
    Sensor8.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor8.objects.count() > 200:
        Sensor8.objects.all().first().delete()

def on_message_sensor9(client, userdata, msg):
    Sensor9.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor9.objects.count() > 200:
        Sensor9.objects.all().first().delete()

def on_message_sensor10(client, userdata, msg):
    Sensor10.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor10.objects.count() > 200:
        Sensor10.objects.all().first().delete()

def on_message_sensor11(client, userdata, msg):
    Sensor11.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor11.objects.count() > 200:
        Sensor11.objects.all().first().delete()

def on_message_sensor12(client, userdata, msg):
    Sensor12.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor12.objects.count() > 200:
        Sensor12.objects.all().first().delete()

def on_message_sensor13(client, userdata, msg):
    Sensor13.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor13.objects.count() > 200:
        Sensor13.objects.all().first().delete()

def on_message_sensor14(client, userdata, msg):
    Sensor14.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor14.objects.count() > 200:
        Sensor14.objects.all().first().delete()

def on_message_sensor15(client, userdata, msg):
    Sensor15.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor15.objects.count() > 200:
        Sensor15.objects.all().first().delete()

def on_message_sensor16(client, userdata, msg):
    Sensor16.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor16.objects.count() > 200:
        Sensor16.objects.all().first().delete()

def on_message_sensor17(client, userdata, msg):
    Sensor17.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor17.objects.count() > 200:
        Sensor17.objects.all().first().delete()

def on_message_sensor18(client, userdata, msg):
    Sensor18.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor18.objects.count() > 200:
        Sensor18.objects.all().first().delete()

def on_message_sensor19(client, userdata, msg):
    Sensor19.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor19.objects.count() > 200:
        Sensor19.objects.all().first().delete()

def on_message_sensor20(client, userdata, msg):
    Sensor20.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor20.objects.count() > 200:
        Sensor20.objects.all().first().delete()

def on_message_sensor21(client, userdata, msg):
    Sensor21.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor21.objects.count() > 200:
        Sensor21.objects.all().first().delete()

def on_message_sensor22(client, userdata, msg):
    Sensor22.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor22.objects.count() > 200:
        Sensor22.objects.all().first().delete()

def on_message_sensor23(client, userdata, msg):
    Sensor23.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor23.objects.count() > 200:
        Sensor23.objects.all().first().delete()

def on_message_sensor24(client, userdata, msg):
    Sensor24.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor24.objects.count() > 200:
        Sensor24.objects.all().first().delete()

def on_message_sensor25(client, userdata, msg):
    Sensor25.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor25.objects.count() > 200:
        Sensor25.objects.all().first().delete()

def on_message_sensor26(client, userdata, msg):
    Sensor26.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor26.objects.count() > 200:
        Sensor26.objects.all().first().delete()

def on_message_sensor27(client, userdata, msg):
    Sensor27.objects.create(value=msg.payload.decode("utf-8"))
    if Sensor27.objects.count() > 200:
        Sensor27.objects.all().first().delete()

def on_message_aktuator1(msg):
    Aktuator1.objects.create(value=str(msg))
    if Aktuator1.objects.count() > 200:
        Aktuator1.objects.all().first().delete()

def on_message_aktuator2(msg):
    Aktuator2.objects.create(value=str(msg))
    if Aktuator2.objects.count() > 200:
        Aktuator2.objects.all().first().delete()

def on_message_aktuator3(msg):
    Aktuator3.objects.create(value=str(msg))
    if Aktuator3.objects.count() > 200:
        Aktuator3.objects.all().first().delete()

def on_message_aktuator4(msg):
    Aktuator4.objects.create(value=str(msg))
    if Aktuator4.objects.count() > 200:
        Aktuator4.objects.all().first().delete()

def on_message_aktuator5(msg):
    Aktuator5.objects.create(value=str(msg))
    if Aktuator5.objects.count() > 200:
        Aktuator5.objects.all().first().delete()

def on_message_aktuator6(msg):
    Aktuator6.objects.create(value=str(msg))
    if Aktuator6.objects.count() > 200:
        Aktuator6.objects.all().first().delete()

def on_message_aktuator7(msg):
    Aktuator7.objects.create(value=str(msg))
    if Aktuator7.objects.count() > 200:
        Aktuator7.objects.all().first().delete()

def on_message_aktuator8(msg):
    Aktuator8.objects.create(value=str(msg))
    if Aktuator8.objects.count() > 200:
        Aktuator8.objects.all().first().delete()

def on_message_aktuator9(msg):
    Aktuator9.objects.create(value=str(msg))
    if Aktuator9.objects.count() > 200:
        Aktuator9.objects.all().first().delete()

def on_message_aktuator10(msg):
    Aktuator10.objects.create(value=str(msg))
    if Aktuator10.objects.count() > 200:
        Aktuator10.objects.all().first().delete()

def on_message_aktuator11(msg):
    Aktuator11.objects.create(value=str(msg))
    if Aktuator11.objects.count() > 200:
        Aktuator11.objects.all().first().delete()

def on_message_aktuator12(msg):
    Aktuator12.objects.create(value=str(msg))
    if Aktuator12.objects.count() > 200:
        Aktuator12.objects.all().first().delete()

def on_message_aktuator13(msg):
    Aktuator13.objects.create(value=str(msg))
    if Aktuator13.objects.count() > 200:
        Aktuator13.objects.all().first().delete()
