from django.forms import ModelForm
from .models import Patient , Appointment


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
