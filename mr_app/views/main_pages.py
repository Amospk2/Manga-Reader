from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from ..models import Manga
from datetime import datetime
# Create your views here.


def home_view(request):
    mockupMangas = [
        Manga(title="Boku No Hero",
        release_date=datetime.now(),
        author="Kōhei Horikoshi",
        description = "Boku no Hero Academia, também conhecido como My Hero Academia no ocidente, é uma série de mangá escrita e ilustrada por Kōhei Horikoshi. Os capítulos do mangá são publicados na revista Weekly Shōnen Jump desde julho de 2014, sendo compilados em volumes formato tankōbon pela editora Shueisha."[0:45],
        tags = " Ficção de aventura, Fantasia científica, História de super-herói, Comédia, Ficção científica",
        image = "bokunohero.jpg"),

        Manga(title="Berserk",
        release_date=datetime.now(),
        author="Kentaro Miura",
        description = 'Berserk é uma série de mangá escrita e ilustrada por Kentaro Miura. Situado em um mundo de fantasia sombria inspirado na Europa medieval, a história gira em torno de Guts, um solitário mercenário, e Griffith, o líder de um bando de mercenários chamado de "Bando do Falcão"'[0:45],
        tags = "Fantasia sombria, Alta fantasia, Espada e feitiçaria",
        image = "wallpaperflare-berserk.jpg"),

        Manga(title="One Punch-Man", 
        release_date=datetime.now(),
        author="Yusuke Murata",
        description = "One Punch-Man é uma série de webcomic criada pelo autor com o pseudónimo One, e é publicada desde 2009. A série rapidamente tornou-se um fenómeno viral, alcançando mais de 7,9 milhões de acessos, em junho de 2012."[0:45],
        tags = "Ação, Comédia, Superhero comics",
        image = "one.jpg"),
    ]

    return render(request, 'main_pages/home.html', {'user': request.user if request.user.is_authenticated else None, 'mangas':mockupMangas})


def about(request):
    return render(request, 'main_pages/about.html', {'user': request.user if request.user.is_authenticated else None})

def categories(request):
    mockupMangas = [
        Manga(title="Boku No Hero",
        release_date=datetime.now(),
        author="Kōhei Horikoshi",
        description = "Boku no Hero Academia, também conhecido como My Hero Academia no ocidente, é uma série de mangá escrita e ilustrada por Kōhei Horikoshi. Os capítulos do mangá são publicados na revista Weekly Shōnen Jump desde julho de 2014, sendo compilados em volumes formato tankōbon pela editora Shueisha."[0:125],
        tags = " Ficção de aventura, Fantasia científica, História de super-herói, Comédia, Ficção científica",
        image = "bokunohero.jpg"),
    ]

    return render(request, 'main_pages/categories.html', {'user': request.user if request.user.is_authenticated else None, 'mangas':mockupMangas})