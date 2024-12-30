from django.shortcuts import render
from careers.models import positions
# Create your views here.
def careers_page(request):
    return render(request ,"careers.html")

def applicationform(request):
    return render(request , "applicationform.html")

def careers_data(request):
    cdata = positions.objects.all().values()
    context = {
        'cdata' :  cdata
    }
    return render(request , "careers_data.html" , context)