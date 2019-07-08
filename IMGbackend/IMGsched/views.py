from django.shortcuts import render,HttpResponse
from rest_framework.decorators import permission_classes
import requests
from . import forms

def signup(request):
    
        form = forms.Userregistration()
        return render(request,'signup.html',{'form':form})
def login(request):
        form = forms.UserLogin()
        return render(request,'login.html',{'form':form})
        

