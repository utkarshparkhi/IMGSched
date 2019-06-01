
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('invitedevents/<int:a>/',views.invited_events_home),
    path('generalevents',views.general_events_home),
    path('<int:id>/<int:event_id>',views.invite_users)
]
