from django.urls import path
from doctors import views
urlpatterns = [
    path('doctors/' , views.doctors_page , name="doctors_page"),
    path('doctorsdata/' , views.doctors_data , name="doctors_data"),
 
]