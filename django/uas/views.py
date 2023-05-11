from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

import paho.mqtt.client as mqtt
from .mqtt import *
from .ml import *

def home(req):
    context = {
        "labels": ["Actuator1","Actuator2"],
        "values": ["200","300"],
    }
    
    return render(req, "index.html", context)

def api(req):
    np_chart = (list((Aktuator13.objects.all())))[190:]
    np_chart_value = ([o.value for o in np_chart])
    np_chart_labels = ([str(o.date_created)[11:19] for o in np_chart])
    data = {
        "Sensor1": serialize("json", list(reversed(Sensor1.objects.all()))),
        "Sensor2": serialize("json", list(reversed(Sensor2.objects.all()))),
        "Sensor3": serialize("json", list(reversed(Sensor3.objects.all()))),
        "Sensor4": serialize("json", list(reversed(Sensor4.objects.all()))),
        "Sensor5": serialize("json", list(reversed(Sensor5.objects.all()))),
        "Sensor6": serialize("json", list(reversed(Sensor6.objects.all()))),
        "Sensor7": serialize("json", list(reversed(Sensor7.objects.all()))),
        "Sensor8": serialize("json", list(reversed(Sensor8.objects.all()))),
        "Sensor9": serialize("json", list(reversed(Sensor9.objects.all()))),
        "Sensor10": serialize("json", list(reversed(Sensor10.objects.all()))),
        "Sensor11": serialize("json", list(reversed(Sensor11.objects.all()))),
        "Sensor12": serialize("json", list(reversed(Sensor12.objects.all()))),
        "Sensor13": serialize("json", list(reversed(Sensor13.objects.all()))),
        "Sensor14": serialize("json", list(reversed(Sensor14.objects.all()))),
        "Sensor15": serialize("json", list(reversed(Sensor15.objects.all()))),
        "Sensor16": serialize("json", list(reversed(Sensor16.objects.all()))),
        "Sensor17": serialize("json", list(reversed(Sensor17.objects.all()))),
        "Sensor18": serialize("json", list(reversed(Sensor18.objects.all()))),
        "Sensor19": serialize("json", list(reversed(Sensor19.objects.all()))),
        "Sensor20": serialize("json", list(reversed(Sensor20.objects.all()))),
        "Sensor21": serialize("json", list(reversed(Sensor21.objects.all()))),
        "Sensor22": serialize("json", list(reversed(Sensor22.objects.all()))),
        "Sensor23": serialize("json", list(reversed(Sensor23.objects.all()))),
        "Sensor24": serialize("json", list(reversed(Sensor24.objects.all()))),
        "Sensor25": serialize("json", list(reversed(Sensor25.objects.all()))),
        "Sensor26": serialize("json", list(reversed(Sensor26.objects.all()))),
        "Sensor27": serialize("json", list(reversed(Sensor27.objects.all()))),
        "Aktuator1": list(reversed(Aktuator1.objects.all()))[0].value,
        "Aktuator2": list(reversed(Aktuator2.objects.all()))[0].value,
        "Aktuator3": list(reversed(Aktuator3.objects.all()))[0].value,
        "Aktuator4": list(reversed(Aktuator4.objects.all()))[0].value,
        "Aktuator5": list(reversed(Aktuator5.objects.all()))[0].value,
        "Aktuator6": list(reversed(Aktuator6.objects.all()))[0].value,
        "Aktuator7": list(reversed(Aktuator7.objects.all()))[0].value,
        "Aktuator8": list(reversed(Aktuator8.objects.all()))[0].value,
        "Aktuator9": list(reversed(Aktuator9.objects.all()))[0].value,
        "Aktuator10": list(reversed(Aktuator10.objects.all()))[0].value,
        "Aktuator11": list(reversed(Aktuator11.objects.all()))[0].value,
        "Aktuator12": list(reversed(Aktuator12.objects.all()))[0].value,
        "Aktuator13": list(reversed(Aktuator13.objects.all()))[0].value,
        "np_chart_value": np_chart_value,
        "np_chart_labels": np_chart_labels,
    }    
    hitung_ml()
    return JsonResponse(data)

def hitung_ml():
    aSensor1 = (list(reversed(Sensor1.objects.all())))[0].value
    aSensor2 = (list(reversed(Sensor2.objects.all())))[0].value
    aSensor3 = (list(reversed(Sensor3.objects.all())))[0].value
    aSensor4 = (list(reversed(Sensor4.objects.all())))[0].value
    aSensor5 = (list(reversed(Sensor5.objects.all())))[0].value
    aSensor6 = (list(reversed(Sensor6.objects.all())))[0].value
    aSensor7 = (list(reversed(Sensor7.objects.all())))[0].value
    aSensor8 = (list(reversed(Sensor8.objects.all())))[0].value
    aSensor9 = (list(reversed(Sensor9.objects.all())))[0].value
    aktuator1 = hitung_aktuator1(aSensor1,aSensor2,aSensor3)
    aktuator2 = hitung_aktuator2(aSensor4,aSensor5,aSensor6)
    aktuator3 = hitung_aktuator3(aSensor7,aSensor8,aSensor9)
    on_message_aktuator1(aktuator1)
    on_message_aktuator2(aktuator2)
    on_message_aktuator3(aktuator3)

    aSensor10 = (list(reversed(Sensor10.objects.all())))[0].value
    aSensor11 = (list(reversed(Sensor11.objects.all())))[0].value
    aSensor12 = (list(reversed(Sensor12.objects.all())))[0].value
    aSensor13 = (list(reversed(Sensor13.objects.all())))[0].value
    aSensor14 = (list(reversed(Sensor14.objects.all())))[0].value
    aSensor15 = (list(reversed(Sensor15.objects.all())))[0].value
    aSensor16 = (list(reversed(Sensor16.objects.all())))[0].value
    aSensor17 = (list(reversed(Sensor17.objects.all())))[0].value
    aSensor18 = (list(reversed(Sensor18.objects.all())))[0].value
    aktuator4 = hitung_aktuator4(aSensor10,aSensor11,aSensor12)
    aktuator5 = hitung_aktuator5(aSensor13,aSensor14,aSensor15)
    aktuator6 = hitung_aktuator6(aSensor16,aSensor17,aSensor18)
    on_message_aktuator4(aktuator4)
    on_message_aktuator5(aktuator5)
    on_message_aktuator6(aktuator6)

    aSensor19 = (list(reversed(Sensor19.objects.all())))[0].value
    aSensor20 = (list(reversed(Sensor20.objects.all())))[0].value
    aSensor21 = (list(reversed(Sensor21.objects.all())))[0].value
    aSensor22 = (list(reversed(Sensor22.objects.all())))[0].value
    aSensor23 = (list(reversed(Sensor23.objects.all())))[0].value
    aSensor24 = (list(reversed(Sensor24.objects.all())))[0].value
    aSensor25 = (list(reversed(Sensor25.objects.all())))[0].value
    aSensor26 = (list(reversed(Sensor26.objects.all())))[0].value
    aSensor27 = (list(reversed(Sensor27.objects.all())))[0].value
    aktuator7 = hitung_aktuator7(aSensor19,aSensor20,aSensor21)
    aktuator8 = hitung_aktuator8(aSensor22,aSensor23,aSensor24)
    aktuator9 = hitung_aktuator9(aSensor25,aSensor26,aSensor27)
    on_message_aktuator7(aktuator7)
    on_message_aktuator8(aktuator8)
    on_message_aktuator9(aktuator9)

    aktuator10 = hitung_aktuator10(aktuator1,aktuator2,aktuator3)
    aktuator11 = hitung_aktuator11(aktuator4,aktuator5,aktuator6)
    aktuator12 = hitung_aktuator12(aktuator7,aktuator8,aktuator9)
    on_message_aktuator10(aktuator10)
    on_message_aktuator11(aktuator11)
    on_message_aktuator12(aktuator12)

    aktuator13 = hitung_aktuator13(aktuator10,aktuator11,aktuator12)
    on_message_aktuator13(aktuator13)

client = mqtt.Client("prauas")
client.message_callback_add('uas/sensor1', on_message_sensor1)
client.message_callback_add('uas/sensor2', on_message_sensor2)
client.message_callback_add('uas/sensor3', on_message_sensor3)
client.message_callback_add('uas/sensor4', on_message_sensor4)
client.message_callback_add('uas/sensor5', on_message_sensor5)
client.message_callback_add('uas/sensor6', on_message_sensor6)
client.message_callback_add('uas/sensor7', on_message_sensor7)
client.message_callback_add('uas/sensor8', on_message_sensor8)
client.message_callback_add('uas/sensor9', on_message_sensor9)
client.message_callback_add('uas/sensor10', on_message_sensor10)
client.message_callback_add('uas/sensor11', on_message_sensor11)
client.message_callback_add('uas/sensor12', on_message_sensor12)
client.message_callback_add('uas/sensor13', on_message_sensor13)
client.message_callback_add('uas/sensor14', on_message_sensor14)
client.message_callback_add('uas/sensor15', on_message_sensor15)
client.message_callback_add('uas/sensor16', on_message_sensor16)
client.message_callback_add('uas/sensor17', on_message_sensor17)
client.message_callback_add('uas/sensor18', on_message_sensor18)
client.message_callback_add('uas/sensor19', on_message_sensor19)
client.message_callback_add('uas/sensor20', on_message_sensor20)
client.message_callback_add('uas/sensor21', on_message_sensor21)
client.message_callback_add('uas/sensor22', on_message_sensor22)
client.message_callback_add('uas/sensor23', on_message_sensor23)
client.message_callback_add('uas/sensor24', on_message_sensor24)
client.message_callback_add('uas/sensor25', on_message_sensor25)
client.message_callback_add('uas/sensor26', on_message_sensor26)
client.message_callback_add('uas/sensor27', on_message_sensor27)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('uas/#')