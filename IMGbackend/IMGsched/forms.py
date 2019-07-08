from django import forms
from django.contrib.auth.models import User
class Userregistration(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')
class UserLogin(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password')
