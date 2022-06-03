from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['Email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        is_staff = None
        if password1=="specialadminpass":
            is_staff = True
        else:
            is_staff =False

        if password1==password2:
            if User.objects.filter(username=username).exists():
                feedback = 'user name taken'
                print('user name taken')
                messages.info(request,'User name taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'Email taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username,first_name=firstname,last_name=lastname, email=email,password = password1,is_superuser=is_staff)
                user.save();
                print('user created')
                return render(request,'signup.html')
        else:
            print('password not matching')
            messages.info(request,'passwords not matching')
            return redirect('/signup')
    else:
       return render(request,'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authinticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request,'login.html')

