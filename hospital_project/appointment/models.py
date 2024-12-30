from django.db import models

# Create your models here.
class appointmentinfo(models.Model):
    patientName = models.CharField(max_length=255)
    contactno = models.IntegerField(null = True)
    emailid = models.CharField(max_length= 255)
    DoctorName = models.CharField(max_length=255)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True)
    fee = models.IntegerField(null=True)
