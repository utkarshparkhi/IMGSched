
from django.contrib import admin
from django.urls import path,include
from . import views
from . import api_view
urlpatterns = [
    path('invitedevents',api_view.invited_events_home),
    path('generalevents',api_view.general_events_home),
    path('generalevents/detail/<int:event_id>',api_view.general_events_detail),
    path('generalevents/comment/<int:event_id>',api_view.general_event_comment),
    path('inviteuser/<int:event_id>/',api_view.invite_users),
    path('invitedevent/details/<int:invited_event_id>',api_view.invited_event_details),
    path('invitedevent/comments/<int:invited_event_id>',api_view.invited_event_comment),
    
    path('signup',views.signup),

  
    path('login',views.login)
    
    
]
