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
    # FILL_ME_IN_OPTIONAL having problems with the event showing up on the calendar? Try mapping Calendar fields
    # with the matching appointment fields ie start appointment.startTime = appointment.startTime.strftime("%Y-%m-%dT%H:%M:%S")
    return render(request, 'tools/FILL_ME_IN.html', {'Appointments': appointments})


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
