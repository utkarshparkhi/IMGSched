
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('invitedevents/<int:a>/',views.invited_events_home),
    path('generalevents',views.general_events_home),
    path('<int:id>/<int:event_id>/inviteuser',views.invite_users),
    path('register/', views.register),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
]
