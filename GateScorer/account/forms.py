from django import forms
from django.contrib.auth.models import User
from home.models import CPerson

class registerUserForm(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=256)
    password=forms.CharField(max_length=32,widget=forms.PasswordInput)
    passwordagain=forms.CharField(max_length=32,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password','passwordagain')