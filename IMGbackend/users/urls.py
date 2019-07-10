from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register,name = "register"),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
    path('getusername/<int:id>',views.get_username),
    path('getall',views.get_all_username)
    
]
