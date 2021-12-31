from django.db import models
from datetime import datetime
# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Room(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=100)

class chatdata(models.Model):
    message=models.CharField(max_length=200000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=1000)
