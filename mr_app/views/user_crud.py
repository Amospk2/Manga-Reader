
from django.contrib import messages
from django.shortcuts import redirect
from ..models import User
from .auth import register_view, login_view, user_crud, edit_view
from .main_pages import home_view


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


    return redirect(home_view)


def edit_user(request, id):
    user = User.objects.get(id=id)
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
        return redirect(edit_view)
    
    user.email = email
    user.username = username
    user.tipo = tipo
    user.dataNascimento = dataNascimento
    user.save()
    
    return redirect(user_crud)

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(user_crud)


def change_type_of_user(request, id):
    user = User.objects.get(id=id)
    user.tipo = "usuário" if user.tipo == "Admin" else "Admin"
    user.save()
    return redirect(user_crud)

