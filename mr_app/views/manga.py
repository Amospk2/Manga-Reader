from django.shortcuts import render
from ..models import User
from ..models import Manga
from datetime import datetime

def manga(request):
    return render(request, 'manga_pages/mangas.html', {'user': request.user if request.user.is_authenticated else None})


def create_manga(request):
    users = User.objects.all()
    return render(request, 'manga_pages/create_manga.html', {'user': request.user if request.user.is_authenticated else None, 'users':users})


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
