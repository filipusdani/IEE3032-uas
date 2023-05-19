from django.db import models

class Sensor1(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Sensor2(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Sensor3(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Aktuator1(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
