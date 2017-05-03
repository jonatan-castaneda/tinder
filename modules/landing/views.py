from django.shortcuts import render, redirect
from .forms import *
#from django.contrib.auth.models import User #For Django Authentication#
from modules.users.models import User
from django.contrib.auth import authenticate, login as iniciar, logout as salir
from django.http import HttpResponse
from .models import Images


# Create your views here.
#For Django Authentication
"""
def index(request):
    images = Images.objects.order_by("-timestamp")
    return render(request, 'landing/index.html',{'request':request,
        'images':images})

def singup(request):
    pass

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                iniciar(request,user)
                return redirect('landing:index')
            else:
                return HttpResponse("Usuario no encontrado")
    return render(request, 'landing/login.html', {"log":form})

def logout(request):
    salir(request)
    return redirect('landing:index')

def uploadImage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)#relaciona el foreign key de la imagen con el user
        if form.is_valid():
            imagen = form.save(commit = False)
            imagen.usuario = request.user
            imagen.save()
            return redirect("landing:index")
    else:
        form = ImageUploadForm()
        return render(request, 'landing/form_imagenes.html', {'form':form})

"""

def index(request):
    images = Images.objects.order_by("-timestamp")
    return render(request, 'landing/index.html',{'request':request,
        'images':images})

def singup(request):
    pass

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                #username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                iniciar(request,user)
                return redirect('landing:index')
            else:
                return HttpResponse("Usuario no encontrado")
    return render(request, 'landing/login.html', {"log":form})

def logout(request):
    salir(request)
    return redirect('landing:index')

def uploadImage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)#relaciona el foreign key de la imagen con el user
        if form.is_valid():
            imagen = form.save(commit = False)
            imagen.usuario = request.user
            imagen.save()
            return redirect("landing:index")
    else:
        form = ImageUploadForm()
        return render(request, 'landing/form_imagenes.html', {'form':form})

def matchs(request):
    
    return render(request, 'landing/matchs.html')