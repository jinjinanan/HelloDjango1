from django.shortcuts import render
from django.shortcuts import redirect
import os

def index(request):
    pass
    return render(request,'Practice1/index.html')

def login(request):
    return render(request,'Practice1/login.html')

def register(request):
    pass
    return render(request,'Practice1/register.html')

def logout(request):
    pass
    return render(request,'/index/')
