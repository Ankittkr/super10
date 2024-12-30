from django.db import models

# Create your models here
class eventsinfo(models.Model):
    eventName = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    date = models.DateField(null=True)
    time = models.TimeField(null = True)
    venue = models.CharField(max_length=255)
    