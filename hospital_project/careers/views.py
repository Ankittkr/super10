from django.shortcuts import render

# Create your views here.
def careers_page(request):
    return render(request ,"careers.html")

def applicationform(request):
    return render(request , "applicationform.html")