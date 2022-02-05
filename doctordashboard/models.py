from django.db import models
import datetime


FULLTIME = 'FT'
PARTTIME = 'PT'
CONTRACT = 'CT'
WORKTYPE = [
        (FULLTIME, 'Full Time'),
        (PARTTIME, 'Part Time'),
        (CONTRACT, 'Contract'),
    ]


class Dentist(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birth = models.DateField(blank=True, null=True)


class Clinic(models.Model):
    dentist = models.OneToOneField(
        Dentist, on_delete=models.CASCADE, primary_key=True)
    clinicName = models.CharField(max_length=100, blank=True, null=True)


class Patient(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    dentist = models.ForeignKey(
        Dentist, blank=True, null=True, on_delete=models.CASCADE)


class Appointment(models.Model):
    ROOTCANAL = 'RC'
    TOOTHEXTRACTIONS = 'TE'
    PULPOTOMY = 'PU'
    BRIDGE = 'BR'
    SURGERIESTYPES = [
        (ROOTCANAL, 'Root Canal'),
        (TOOTHEXTRACTIONS, 'Tooth Extraction'),
        (PULPOTOMY, 'Pulpotomy'),
        (BRIDGE, 'Bridge'),
    ]
    appointmentPurpose = models.CharField(
        blank=True, null=True,
        max_length=2,
        choices=SURGERIESTYPES,
        default=ROOTCANAL,
    )
    patientName = models.OneToOneField(
        Patient, on_delete=models.CASCADE, primary_key=True, blank=True , default="")
    DentistName = models.OneToOneField(
        Dentist, on_delete=models.CASCADE, blank=True, null=True)
    operationPrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    datetime = models.DateTimeField(
        blank=True, default=datetime.date.today, null=False)


class Balance(models.Model):
    dentist = models.OneToOneField(
        Dentist, on_delete=models.CASCADE, primary_key=True)
    totalBalance = models.DecimalField(
        max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    pendingBalance = models.DecimalField(
        max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)


class AmountDue(models.Model):
    dentist = models.OneToOneField(
        Dentist, on_delete=models.CASCADE, primary_key=True)
    Patient = models.OneToOneField(
        Patient, on_delete=models.CASCADE)
    AmountDue = models.DecimalField(
        max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)


class Nurse(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    workingHours = models.DecimalField(max_digits=2, default=0.00, decimal_places=0, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    clinic = models.OneToOneField(
        Clinic, blank=True, null=True, on_delete=models.CASCADE)
    workType = models.CharField(
        blank=True, null=True,
        max_length=2,
        choices=WORKTYPE,
        default=FULLTIME,
    )

class Secretary(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    workingHours = models.DecimalField(max_digits=2, default=0.00, decimal_places=0, blank=True, null=True)
    salary = models.DecimalField(
        max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    clinic = models.OneToOneField(
        Clinic, blank=True, null=True, on_delete=models.CASCADE)
    workType = models.CharField(
        blank=True, null=True,
        max_length=2,
        choices=WORKTYPE,
        default=FULLTIME,
    )

class Administrator(models.Model):
    firstName = models.CharField(max_length=100, blank=True, null=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    workingHours = models.DecimalField(max_digits=2, default=0.00, decimal_places=0, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, default=0.00, decimal_places=2, blank=True, null=True)
    clinic = models.OneToOneField(
        Clinic, blank=True, null=True, on_delete=models.CASCADE)
    workType = models.CharField(
        blank=True, null=True,
        max_length=2,
        choices=WORKTYPE,
        default=FULLTIME,
    )
