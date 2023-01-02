import os
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required, permission_required
from .utils import *

@login_required(login_url='/login')
def manga(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_pages/mangas.html', {'user': check_if_has_user_activate(request), 'mangas':mangas})

@login_required(login_url='/login')
@permission_required('mr_app.add_manga', raise_exception=True)
def create_manga(request, form={}):
    users = User.objects.all()
    return render(request, 'manga_pages/create_manga.html', {'user': check_if_has_user_activate(request), 'users':users, 'form':form})

@login_required(login_url='/login')
def edit_manga(request, id):
    users = User.objects.all()
    form = Manga.objects.get(id=id)
    tags = form.tags
    if request.user in form.managers.all() or request.user.has_perm('mr_app.change_manga'):
        return render(request, 'manga_pages/edit_manga.html', {'user': check_if_has_user_activate(request), 'users':users, 'form':form, 'tags':tags, 'id':id})
    return HttpResponseRedirect('/')

def details(request, id):
    manga = Manga.objects.get(id=id)
    manga.tags = manga.tags.split(',')
    return render(request, 'manga_pages/details.html', {'user': check_if_has_user_activate(request), 'manga':manga, 'capitulos':manga.capitulo_set.all()})


@login_required(login_url='/login')
def create_new_manga(request):
    try:
        manga = Manga.objects.create(
            title=request.POST.get('name'),
            release_date=request.POST.get('release_date'),
            author=request.POST.get('author_name'),
            description=request.POST.get('description'),
            tags=request.POST.get('tags'),
            image=request.FILES['images[]']
        )
        for user in request.POST.get('managers').split(','):
            manga.managers.add(User.objects.get(username=user))
        manga.save()
    except MultiValueDictKeyError as ex:
        messages.error(request=request, message="Você deve escolhar uma imagem para o manga!")
        users = User.objects.all()
        form = Manga.objects.get(id=id)
        tags = form.tags
        return render(request, 'manga_pages/edit_manga.html', {'user': check_if_has_user_activate(request), 'users':users, 'form':form, 'tags':tags})

    except Exception as ex:
        messages.error(request=request, message="Já existe um manga com este nome!")
        users = User.objects.all()
        form = Manga.objects.get(id=id)
        tags = form.tags
        return render(request, 'manga_pages/edit_manga.html', {'user': check_if_has_user_activate(request), 'users':users, 'form':form, 'tags':tags})


    return HttpResponseRedirect('/manga')


@login_required(login_url='/login')
@permission_required('mr_app.change_manga', raise_exception=True)
def update_manga(request):
    try:
        manga = Manga.objects.get(id=request.POST.get('id'))
        os.remove(manga.image.path)
        manga.title=request.POST.get('name')
        manga.release_date=request.POST.get('release_date')
        manga.author=request.POST.get('author_name')
        manga.description=request.POST.get('description')
        manga.tags=request.POST.get('tags')
        manga.image=request.FILES['images[]']
        manga.save()
        
    except MultiValueDictKeyError as ex:
        messages.error(request=request, message="Você deve escolhar uma imagem para o manga!")
        return erro_on_update(request, request.POST.get('id'))

    return HttpResponseRedirect('/manga')



def erro_on_update(request, id):
    users = User.objects.all()
    form = Manga.objects.get(id=id)
    tags = form.tags
    return render(request, 'manga_pages/edit_manga.html', {'user': check_if_has_user_activate(request), 'users':users, 'form':form, 'tags':tags, 'id':id})


@login_required(login_url='/login')
def delete_manga(request, id):
    manga = Manga.objects.get(id=id)
    manga.delete()
    return HttpResponseRedirect('/manga')