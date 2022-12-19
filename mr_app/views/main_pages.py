from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from ..models import User
# Create your views here.


def home_view(request):
    return render(request, 'main_pages/home.html', {'user': request.user if request.user.is_authenticated else None})


def details(request):
    return render(request, 'main_pages/details.html', {'user': request.user if request.user.is_authenticated else None})

def about(request):
    return render(request, 'main_pages/about.html', {'user': request.user if request.user.is_authenticated else None})

def categories(request):
    return render(request, 'main_pages/categories.html', {'user': request.user if request.user.is_authenticated else None})