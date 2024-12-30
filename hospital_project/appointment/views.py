from django.shortcuts import render
from appointment.models import appointmentinfo
# Create your views here.
def appointment(request):
    return render(request , "appointment.html")

def appointment_data(request):
    adata = appointmentinfo.objects.all().values()
    context = {
        "adata" : adata
    }
    return render(request ,"appointment_data.html" , context )