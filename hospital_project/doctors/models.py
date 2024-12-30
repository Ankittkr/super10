from django.db import models

# Create your models here.
class doctorsinfo(models.Model):
    docName = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)
    contact = models.IntegerField(null = True)
    emailId = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    exp =  models.CharField(max_length=255)
    achievement = models.CharField(max_length = 255)
    fee = models.IntegerField(null = True)
