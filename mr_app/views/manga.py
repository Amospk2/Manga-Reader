import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..models import *
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError

def manga(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_pages/mangas.html', {'user': request.user if request.user.is_authenticated else None, 'mangas':mangas})


def create_manga(request, form={}):
    users = User.objects.all()
    return render(request, 'manga_pages/create_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form})


def edit_manga(request, id):
    users = User.objects.all()
    form = Manga.objects.get(id=id)
    tags = form.tags
    return render(request, 'manga_pages/edit_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form, 'tags':tags, 'id':id})


def view_chapter(request, id):
    users = User.objects.all()
    return render(request, 'manga_pages/view_chapter.html', {'user': request.user if request.user.is_authenticated else None, 'users':users})


def details(request, id):
    manga = Manga.objects.get(id=id)
    manga.tags = manga.tags.split(',')
    return render(request, 'manga_pages/details.html', {'user': request.user if request.user.is_authenticated else None, 'manga':manga, 'capitulos':manga.capitulo_set.all()})



def create_new_manga(request):
    try:
        Manga.objects.create(
            title=request.POST.get('name'),
            release_date=request.POST.get('release_date'),
            author=request.POST.get('author_name'),
            description=request.POST.get('description'),
            tags=request.POST.get('tags'),
            image=request.FILES['images[]']
        )
    except MultiValueDictKeyError as ex:
        messages.error(request=request, message="Você deve escolhar uma imagem para o manga!")
        users = User.objects.all()
        form = Manga.objects.get(id=id)
        tags = form.tags
        return render(request, 'manga_pages/edit_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form, 'tags':tags})

    except Exception as ex:
        messages.error(request=request, message="Já existe um manga com este nome!")
        users = User.objects.all()
        form = Manga.objects.get(id=id)
        tags = form.tags
        return render(request, 'manga_pages/edit_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form, 'tags':tags})


    return HttpResponseRedirect('/manga')

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

def erro_on_create(request, template):
    users = User.objects.all()
    return render(request, template, {'user': request.user if request.user.is_authenticated else None, 'users':users, 
    'form':{
        'name':request.POST.get('name'),
        'release_date':request.POST.get('release_date'),
        'author_name':request.POST.get('author_name'),
        'description':request.POST.get('description'),
        }
    })


def erro_on_update(request, id):
    users = User.objects.all()
    form = Manga.objects.get(id=id)
    tags = form.tags
    return render(request, 'manga_pages/edit_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form, 'tags':tags, 'id':id})


def delete_manga(request, id):
    manga = Manga.objects.get(id=id)
    manga.delete()

    return HttpResponseRedirect('/manga')