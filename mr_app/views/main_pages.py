from django.shortcuts import render
from ..models import Manga
from datetime import datetime
from .utils import *
from ..models import *

def home_view(request):
    return render(request, 'main_pages/home.html', {'user': check_if_has_user_activate(request), 'mangas':Manga.objects.all()})


def about(request):
    return render(request, 'main_pages/about.html', {'user': check_if_has_user_activate(request)})

def categories(request, id=None):
    mangas = Manga.objects.all()
    if(not id or id == 1):
        mangas = mangas[0:10]
    else:
        mangas = mangas[(id-1)*10:id*10]

    count_mangas = []
    for i in range(100):
        if(i%10 == 0 and i>0):
            count_mangas.append(i+1 if i == 0 else int(i/10))

    return render(request, 'main_pages/categories.html', {'user': check_if_has_user_activate(request), 'mangas':mangas, 'count_manga': count_mangas}) 

