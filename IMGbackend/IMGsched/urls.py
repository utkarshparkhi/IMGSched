
from django.contrib import admin
from django.urls import path,include
from . import views
from . import api_view
urlpatterns = [
    path('invitedevents',api_view.invited_events_home),
    path('generalevents',api_view.general_events_home),
    path('generalevents/detail',api_view.general_events_detail),
    path('inviteuser/<int:event_id>/',api_view.invite_users),
    path('invitedevent/details',api_view.invited_event_details),
    path('signup',views.signup),

  
    path('login',views.login)
    
    
]
