from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import \
    login as log_in, logout as log_out
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/login?redirect_error=403')
def index(request):
    return HttpResponse('Hello, user! Here will be your information')


def login(request):
    # if POST -> log_in by special backend with
    pass


@login_required(login_url='/user/login?redirect_error=403')
def logout(request):
    log_out(request)
    return redirect('/')

