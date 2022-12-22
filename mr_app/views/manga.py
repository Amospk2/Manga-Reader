from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from ..models import User
from ..models import Manga
from datetime import datetime

def manga(request):
    mangas = Manga.objects.all()
    return render(request, 'manga_pages/mangas.html', {'user': request.user if request.user.is_authenticated else None, 'mangas':mangas})


def create_manga(request, form={}):
    users = User.objects.all()
    return render(request, 'manga_pages/create_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'form':form})


def create_chapter(request, id):
    users = User.objects.all()
    return render(request, 'manga_pages/create_chapter.html', {'user': request.user if request.user.is_authenticated else None, 'users':users})


def view_chapter(request, id):
    users = User.objects.all()
    return render(request, 'manga_pages/view_chapter.html', {'user': request.user if request.user.is_authenticated else None, 'users':users})


def details(request, id):
    manga = Manga(title="Boku No Hero",
    release_date=datetime.now(),
    author="Kōhei Horikoshi",
    description = "Boku no Hero Academia, também conhecido como My Hero Academia no ocidente, é uma série de mangá escrita e ilustrada por Kōhei Horikoshi. Os capítulos do mangá são publicados na revista Weekly Shōnen Jump desde julho de 2014, sendo compilados em volumes formato tankōbon pela editora Shueisha.",
    tags = " Ficção de aventura, Fantasia científica, História de super-herói, Comédia, Ficção científica",
    image = "bokunohero.jpg")

    manga.tags = manga.tags.split(',')
    return render(request, 'manga_pages/details.html', {'user': request.user if request.user.is_authenticated else None, 'manga':manga})



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
    except:
        messages.error(request=request, message="Já existe um manga com este nome!")
        users = User.objects.all()
        return render(request, 'manga_pages/create_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 
        'form':{
            'name':request.POST.get('name'),
            'release_date':request.POST.get('release_date'),
            'author_name':request.POST.get('author_name'),
            'description':request.POST.get('description'),
            'tags':request.POST.get('tags'),
            'image':request.FILES['images[]']
            }
        })


    return HttpResponseRedirect('/manga')

def delete_manga(request, id):
    manga = Manga.objects.get(id=id)
    manga.delete()

    return HttpResponseRedirect('/manga')