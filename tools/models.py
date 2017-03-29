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
    patient = models.ForeignKey( 'Patient', default=None,  )
    #FILL_ME_IN what variables do we need to create an appointment for Full Calendar

    def __str__(self):
        return str(self.name)
