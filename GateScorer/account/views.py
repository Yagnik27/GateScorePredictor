from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from home.models import CPerson
from . import forms

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return HttpResponse('You\'re on accounts page' )

class signupUser(View):
    temp_name='accounts/signup.html'
    message=""
    def post(self,request):
        form=forms.registerUserForm(request.POST)
        if form.is_valid() and form.cleaned_data['password']==form.cleaned_data['passwordagain']:
            username=form.cleaned_data['username']
            try:
                user=User.objects.get(username=username)
                message="Username Exists!! Try another"
                form=forms.registerUserForm()
                return render(request,'account/login.html',{'message':message,'form':form,})
            except:
                email=form.cleaned_data['email'] 
                password=form.cleaned_data['password']
                password=make_password(password,salt=None,hasher='default')
                user=User(username=username,email=email,password=password)
                user.save()
                person=CPerson(user=user)
                person.save()
                #wel_message='Hi'+username+'.'+'Welcome to JDPTUTS.Let us learn for a better future' 
                #send_mail('Welcome',
                 #        wel_message,
                  #       settings.EMAIL_HOST_USER,
                   #      [email],
                    #     fail_silently=False)
                login(request,user)
                return redirect('home:hindex')
        else:
            message="Check whether password and confirm password field are same or not"
            form=forms.registerUserForm()
            return render(request,'account/login.html',{'message':message,'form':form,})   
                
#@never_cache
class loginUser(View):
    temp_name='account/login.html'
    @never_cache
    def get(self,request):
        if request.user.is_authenticated==True:
            return redirect('home:hindex')
        else:
            form=forms.registerUserForm()
            return render(request,self.temp_name,{'form':form})
    @never_cache
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('home:hindex')
        else:
            message="Please enter correct username and password"
            return render(request,self.temp_name,{'message':message,})
    
    
class logout_user(View):
    @never_cache
    def post(self,request):
        logout(request)
        return redirect('account:login')
    
    