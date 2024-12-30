from django.shortcuts import render
from doctors.models import doctorsinfo
# Create your views here.
def doctors_page(request):
    return render(request,"doctors.html")

def doctors_data(request):
    ddata = doctorsinfo.objects.all().values()
    context = {
        "ddata" :  ddata
    }
    return render(request, "doctors_data.html" , context)
