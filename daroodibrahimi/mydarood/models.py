from django.db import models


# Create your models here.

class todaydata(models.Model):
    name =  models.CharField(default="Muhammad Ali")
    recited = models.IntegerField()
    eventDate = models.DateField()
