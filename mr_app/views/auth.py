from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from ..models import User
from .main_pages import home_view
# Create your views here.


def is_guess(use):
    if not use.is_authenticated:
        return True
    else:
        return False

def login_view(request):
    return render(request, 'auth/login.html') if is_guess(request.user) else redirect(home_view)


def register_view(request):
    return render(request, 'auth/register.html') if is_guess(request.user) else redirect(home_view)


def logout_view(request):
    logout(request)
    return redirect(login_view)


def auth(request):
    username =request.POST.get('email')
    senha = request.POST.get('password')

    if(username is not None and senha is not None):
        user = authenticate(username=username, password=senha)
    else:
        messages.error(request=request, message="Preenche essa merda")
        return render(request, 'auth/login.html')

    if user is not None:
        login(request, user)
        return redirect(home_view)
    else:
        messages.error(request=request, message="Informações incorretas")
        return render(request, 'auth/login.html')

def create_new_user(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    tipo = "usuário"
    dataNascimento = request.POST.get('dataNascimento')
    senha = request.POST.get('password')
    confirmarsenha = request.POST.get('confirmpassword')

    if(email != None and username != None  and tipo != None and dataNascimento   != None and senha != None):
        messages.error(request=request, message="Preencha todos os campos")

    if(senha != confirmarsenha):
        messages.error(request=request, message="As senha não coicidem.")
        return redirect(register_view)
    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.tipo = tipo
    user.dataNascimento = dataNascimento
    user.save()
    
    return redirect(login_view)