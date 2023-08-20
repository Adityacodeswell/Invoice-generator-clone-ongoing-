from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import *

def Home(request):
    return render(request,'home.html',{})


@login_required(login_url= '/login/')
def home(request):
    return render(request, 'home.html')


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

def invoice(request):
    if request.method == 'POST':
        comp_name = request.POST.get('comp_name')
        gst = request.POST.get('gst')
        country = request.POST.get('country')
        state = request.POST.get('state')
        address = request.POST.get('address')

        user = Client.objects.create(
            user=request.user,
            comp_name=comp_name,
            gst=gst,
            country=country,
            state=state,
            address=address,
        )
        user.save()
        return render(request, 'invoicegen.html')  # Successful response after saving
    
    return render(request, 'invoicegen.html')
    
   

def add_service(request):
    form = ClientData()
    serviceObj = Add_service.objects.all()
    if request.method == 'POST':
        
        form = ClientData(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addService')

        client = request.POST.get('client')
        comp2_name = request.POST.get('comp2_name')
        handle_by = request.POST.get('handle_by')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        account = request.POST.get('account')

        user = Add_service.objects.create(
            client = client,
            comp2_name = comp2_name,
            handle_by = handle_by,
            email = email,
            phone = phone,
            account = account,
        )
        user.save()
        # queryset = Add_service.objects.all()
        # context = {'service' : queryset}
    return render(request, 'addService.html', {'form': form, 'serviceObj':serviceObj})

def service(request):
    servicefm = ServiceForm()
    if request.method == 'POST':
        servicefm = ServiceForm(request.POST)
        if servicefm.is_valid():
            servicefm.save()
            return redirect('service')
        client = request.POST.get('client')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')

        user = Service.objects.create(
            client = client,
            description = description,
            quantity = quantity,
            amount = amount,
        )
        user.save()
    return render(request, 'service.html', {'servicefm': servicefm})


