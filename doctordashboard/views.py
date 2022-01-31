from django.shortcuts import render
from .forms import AppointmentForm , PatientForm
from .models import Appointment , Patient
# Create your views here.

def index(request):
    return render(request , 'index.html')


def dentistDashboard(request):
    return render(request, 'dentistdashboard.html')


def addpatient(request):
    form = PatientForm()
    
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'addpatient.html', context)


def patientlist(request):
    patients_list = Patient.objects.all()
    context = {
        'patients_list': patients_list,
    }
    return render(request, 'patientlist.html' , context)


def addappointment(request):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    
    return render(request, 'addappointment.html' , context)


def appointmentslist(request):
    appointmentslist = Appointment.objects.all()
    context = {
        'appointmentslist': appointmentslist,
    }
    return render(request, 'appointmentslist.html' , context)
