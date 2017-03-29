from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from tools.models import Patient, Appointment
from tools.forms import PatientForm, AppointmentForm

def index(request):
    patients = Patient.objects.all()
    return render(request, 'tools/index.html', {'tools': patients})


def detail(request, tool_id):
    patient = get_object_or_404(Patient, pk=tool_id)
    return render(request, 'tools/detail.html', {'tool': patient})


def calendar(request):
    appointments = Appointment.objects.all()
    for app in appointments:
        start = app.startTime
        end = app.endTime
        app.startTime = start.strftime("%Y-%m-%dT%H:%M:%S")
        app.endTime = end.strftime("%Y-%m-%dT%H:%M:%S")
    return render(request, 'tools/calendar.html', {'Appointments': appointments})


class CreateAppointment(CreateView):

    model = Appointment
    template_name = 'tools/appointment_form.html'

    form_class = AppointmentForm


class CreatePatient(CreateView):

    model = Patient
    template_name = 'tools/tool_form.html'

    form_class = PatientForm


class EditPatient(UpdateView):
    
    model = Patient
    template_name = 'tools/tool_form.html'

    form_class = PatientForm
