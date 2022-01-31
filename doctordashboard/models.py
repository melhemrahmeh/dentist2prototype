from django.db import models
import datetime

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)

    

class Appointment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    operation_price = models.IntegerField(default=0 , blank=True, null=True)
    datetime = models.DateTimeField(blank=True, default=datetime.date.today , null=False)
    cause = models.CharField(blank=True, null=True , max_length=300)
