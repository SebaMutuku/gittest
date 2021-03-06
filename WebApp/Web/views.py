# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Web import forms
from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'Web/login.html')


def login(request):
    if request.method == 'POST':
        form = forms.userLogin(data=request.POST)

    else:
        form = forms.userLogin()
    return render(request, 'Web/login.html', {'form': form})


def SignUp(request):
    if request.method == "POST":
        form = forms.userRegisteration(data=request.POST)
    else:
        form = forms.userRegisteration()
    return render(request, 'Web/SignUp.html', {'form': form})


def error_404(request):
    context = {'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_404.html', context)


def error_500(request):
    context = {
        'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_500.html', context)


def error_400(request):
    context = {'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_400.html', context)


def error_403(request):
    context = {'project_name': settings.PROJECT_NAME}
    return render(request, 'Web/error_404.html', context)


def Reset(request):
    if request.method=='POST':
        form=forms.ResetPass(data=request.POST)
    context={
        'project_name':settings.PROJECT_NAME

    }
    return render(request,'Web/resetPass.html',context,{'form': form})
