from django.urls import path
from appointment import views
urlpatterns = [
    path('appointment/' , views.appointment , name="appointment"),
    path('appointmentdata/' , views.appointment_data, name="appointment_data"),

]