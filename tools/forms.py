from django import forms
from tools.models import Patient, Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        patient = forms.CharField()
        description = forms.CharField()
        isAvailable = forms.BooleanField()
        fields = ['name', 'description', 'isAvailable']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        patient = forms.ChoiceField()
        #FILL_ME_IN What do Appointments do?
        fields = ['patient']