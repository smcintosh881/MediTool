from django.db import models
from datetime import datetime

class Patient(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    patient = models.CharField(max_length=50)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

class Appointment(models.Model):
    notes = models.CharField( max_length = 500,  default=None )
    patient = models.ForeignKey( 'Patient', default=None,  )
    startTime = models.DateTimeField("Appointment Date (YYYY-MM-DD HH:MM)", null=True)
    endTime = models.DateTimeField("Appointment Date (YYYY-MM-DD HH:MM)", null=True)

    def __str__(self):
        return str(self.name)
