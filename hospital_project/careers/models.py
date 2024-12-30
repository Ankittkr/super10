from django.db import models

# Create your models here.  
class positions(models.Model):
    positionName = models.CharField(max_length=255)
    hrName = models.CharField(max_length=255)
    openingdate = models.DateField(null=True)
    closeddate = models.DateField(null=True)
    notes = models.CharField(max_length=500)
    status = models.IntegerField(null=True)
    deparment = models.CharField(max_length=500)
    baseSalary = models.IntegerField(null = True)
    hiringManager = models.CharField(max_length=255)
