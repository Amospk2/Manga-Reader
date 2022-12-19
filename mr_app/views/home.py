from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from ..models import User
# Create your views here.


def home_view(request):
    return render(request, 'views/home.html', {'user': request.user if request.user.is_authenticated else None})


def details(request):
    return render(request, 'views/details.html')