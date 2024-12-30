from django.shortcuts import render , HttpResponse
from events.models import eventsinfo

# Create your views here.
def index(request):
    return render(request , "index.html")

def events_data(request):
    edata = eventsinfo.objects.all().values()
    context = {
        'edata' : edata
    }
    return render(request , "events_data.html" , context )
