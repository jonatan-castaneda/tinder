from django.shortcuts import render, redirect
from .forms import *
#from django.contrib.auth.models import User #For Django Authentication#
from modules.users.models import User
from django.contrib.auth import authenticate, login as iniciar, logout as salir
from django.http import HttpResponse
from .models import Images
import requests
import random


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

class Distancia:
    def peticion(self):
        q=["19.426112,-99.186206","19.423239,-99.189511","19.424763,-99.195070","19.440073,-99.203649","19.429493,-99.132244","19.412264,-99.168174","19.429140,-99.197024","19.437611,-99.072726","19.321405,-99.185096","19.355143,-99.162579"]
        o=(random.choice(q))
        d=(random.choice(q))
        a=requests.get(params={"origins": o, "destinations":d}, url="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&key=AIzaSyBfI7bob5KZFrPC4kQ-tzZzE63airiYsqU").json()
        self.direco=a["destination_addresses"][0]
        self.direcd=a["origin_addresses"][0]
        self.distancia=a["rows"][0]["elements"][0]["distance"]["text"]
        self.tiempo=a["rows"][0]["elements"][0]["duration"]["text"]
        print ("Origen "+self.direco)
        print ("Destino "+self.direcd)
        print ("Distancia es "+self.distancia)
        print ("El tiempo es "+self.tiempo)

def index(request):
    images = Images.objects.order_by("-timestamp")
    return render(request, 'landing/index.html',{'request':request,
        'images':images})

def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data.pop('confirm_password', None)
            user = User.objects.create_user(**form.cleaned_data)
            return redirect("landing:index")
    
    return render(request,'landing/sign.html',{'sign':form})

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
    dir=Distancia()
    dir.peticion()
    
    return render(request, 'landing/matchs.html', {'distancia':'250 metros'})


