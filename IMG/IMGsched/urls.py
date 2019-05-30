
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('invitedevents/<int:a>/',views.invited_events),
    path('generalevents',views.general_events)
]
