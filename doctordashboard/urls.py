from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dentistDashboard/', views.dentistDashboard),
    path('addpatient/', views.addpatient),
    path('patientlist/', views.patientlist),    
    path('addappointment/', views.addappointment),
    path('appointmentslist/', views.appointmentslist), 
    ]
