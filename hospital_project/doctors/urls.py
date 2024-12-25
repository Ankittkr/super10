from django.urls import path
from doctors import views
urlpatterns = [
    path('doctors/' , views.doctors_page , name="doctors_page"),
]