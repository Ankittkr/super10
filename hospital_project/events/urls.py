from django.urls import path
from events import views
urlpatterns = [
    path('' , views.index , name="temp"),
    path('eventsdata' , views.events_data , name="events_data"),

]