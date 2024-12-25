from django.urls import path
from careers import views
urlpatterns = [
    path('careers/' , views.careers_page , name="careers_page"),
    path('careers/applicationform/' , views.applicationform , name="applicationform"),
]