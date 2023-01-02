
from django.contrib import messages
from django.shortcuts import redirect, render
from ..models import User, Manga, Capitulo
from .auth import register_view, edit_view
from .main_pages import home_view
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required
from .utils import *

@login_required
@permission_required(perm='mr_app.change_user', raise_exception=True)
def user_crud(request):
    users = User.objects.all()
    return render(request, 'auth/user_crud.html', {'user': check_if_has_user_activate(request), 'users':users, 'user_has_all_perms':request.user.has_perms(['user.add_user', 'user.change_user', 'user.delete_user', 'user.view_user'])})

    
def create_new_user(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    type = "usuário"
    dataNascimento = request.POST.get('dataNascimento')
    senha = request.POST.get('password')
    confirmarsenha = request.POST.get('confirmpassword')

    if(email != None and username != None  and type != None and dataNascimento   != None and senha != None):
        messages.error(request=request, message="Preencha todos os campos")
        return redirect(register_view)

    if(senha != confirmarsenha):
        messages.error(request=request, message="As senha não coicidem.")
        return redirect(register_view)
    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.type = type
    user.dataNascimento = dataNascimento
    user.save()


    return redirect(home_view)



def edit_user(request, id):
    user = User.objects.get(id=id)
    email = request.POST.get('email')
    username = request.POST.get('username')
    type = "usuário"
    dataNascimento = request.POST.get('dataNascimento')
    senha = request.POST.get('password')
    confirmarsenha = request.POST.get('confirmpassword')

    if(email != None and username != None  and type != None and dataNascimento   != None and senha != None):
        messages.error(request=request, message="Preencha todos os campos")

    if(senha != confirmarsenha):
        messages.error(request=request, message="As senha não coicidem.")
        return redirect(edit_view)
    
    user.email = email
    user.username = username
    user.type = type
    user.dataNascimento = dataNascimento
    user.save()
    
    return redirect(user_crud)

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(user_crud)


def change_type_of_user(request, id):
    user_permissions = get_permision_from_model(User)
    manga_permissions = get_permision_from_model(Manga)
    capitulo_permissions = get_permision_from_model(Capitulo)
    user = User.objects.get(id=id)
    if(user.type == "usuário"):
        for perm in user_permissions:
            user.user_permissions.add(perm)
        for perm in manga_permissions:
            user.user_permissions.add(perm)
        for perm in capitulo_permissions:
            user.user_permissions.add(perm)
    else:
        for perm in user_permissions:
            user.user_permissions.remove(perm)
        for perm in manga_permissions:
            user.user_permissions.remove(perm)
        for perm in capitulo_permissions:
            user.user_permissions.remove(perm)  
    user.type = "usuário" if user.type == "Admin" else "Admin"
    user.save()
    return redirect(user_crud)


def get_permision_from_model(model):
    content_type = ContentType.objects.get_for_model(model=model)
    return Permission.objects.filter(content_type=content_type)