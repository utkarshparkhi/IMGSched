
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('invitedevents',views.invited_events_home),
    path('generalevents',views.general_events_home),
    path('inviteuser/<int:event_id>',views.invite_users),
    path('invitedevent/details',views.invited_event_details)
    
]
