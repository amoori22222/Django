from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse, response
from .models import Service, Project, Contact
# Create your views here.

def index(request):


    services = Service.objects.all()

    projects = Project.objects.all()
    
    contacts = Contact.objects.all()

    return render(request, 'index.html', {'services':services,'projects':projects,'contacts':contacts})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password == password_confirmation :
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName Already exists')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already exists')
                return redirect('/register')
            else:
                add_user = User.objects.create_user(username= username, email=email, password=password)
                add_user.save()
                return redirect('/')
        elif password != password_confirmation :
            messages.info(request,'password not the same')
            return redirect('/register')
        else:
            messages.info(request,'u must fill the form')
            return redirect('/register')

    return render(request, 'register.html')

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        elif user is None:
            messages.info(request, 'user not exists')
            return redirect('login')
    
    return render(request,'login.html')