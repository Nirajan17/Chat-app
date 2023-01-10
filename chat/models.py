from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date_time = models.DateTimeField(default = datetime.now,blank=True)
    username = models.CharField(max_length=1000)
    room_to_send = models.CharField(max_length=1000)