from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def loging(request):
    return render(request,'login.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authinticate(username=username , password=password)
        if user is not None:
            print('not none')
            auth.login(request,user)
            return redirect('')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    else:
        return render(request,'login.html')
