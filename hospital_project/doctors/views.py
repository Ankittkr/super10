from django.shortcuts import render

# Create your views here.
def doctors_page(request):
    return render(request,"doctors.html")