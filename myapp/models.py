from django.db import models

class Temperature_db(models.Model):
    myid = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField(null=False)
    temperature = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    timestamp = models.DateTimeField(auto_now=True)

# Create your models here.
