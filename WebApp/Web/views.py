# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm
from django.shortcuts import render
from django.conf import  settings


# Create your views here.
def home(request):
    return render(request,'Web/home.html')

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)

    else:
        form=AuthenticationForm()
    return  render(request,'Web/login.html',{'form':form})

def SignUp(request):
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
    else:
        form=UserCreationForm()
    return  render(request,'Web/SignUp.html',{'form':form})

def error_404(request):
    context={'project_name':settings.PROJECT_NAME}
    return render(request,'Web/error_404,html',context)


def error_500(request):
    context = {'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_500,html', context)

