from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import *

def Home(request):
    return render(request,'home.html',{})


@login_required(login_url= '/login/')
def home(request):
    return render(request, 'home.html')

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid/Incorrect Username or Password')
            return redirect('/login/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')

def Signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'This username is already exist')
            return redirect('/signup/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created Successfulyy!!')
        return redirect('home')
    return render(request, 'signup.html')