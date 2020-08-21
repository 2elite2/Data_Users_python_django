from django.shortcuts import render, redirect,  HttpResponseRedirect
from datetime import datetime
from log.models import Member #models.py
from django.contrib import messages
 
# Create your views here.
def index(request):

    if request.method == "POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       phone=request.POST.get('phone')
       password=request.POST.get('password')
       index = Member(name=name, email=email, phone=phone, password=password, date=datetime.today())
       index.save()
       messages.success(request, 'Your Asean Tax account has been created ')
       return redirect('/')
    else:
        return render(request, 'index.html')
 

        
def login(request):
    return render(request, 'login.html')

 
def home(request):

    if request.method == "POST":
        if Member.objects.filter(phone=request.POST['phone'], password=request.POST['password']).exists():
            member = Member.objects.get(phone=request.POST['phone'], password=request.POST['password'])
            messages.success(request, 'Your Asean Tax account has been created ')
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
    

def select(request):
    return render(request, 'select.html')

    
