from django.utils.datastructures import MultiValueDictKeyError
from ..models import Manga, User, Capitulo, Page
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect

def create_new_chapter(request, id):

    try:
        capitulo = Capitulo(
            fk_manga=Manga.objects.get(id=7),
            title=request.POST.get('name'),
            release_date=request.POST.get('release_date'),
            description=request.POST.get('description'),
        )
        capitulo.save()

        for index, value in enumerate(request.FILES.getlist('images[]')):
            Page.objects.create(
                fk_capitulo=capitulo,
                title=capitulo.title + "_" + str(index),
                file=value
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
    
    return HttpResponseRedirect('/manga/details/'+id)

def create_chapter(request, id):
    users = User.objects.all()
    return render(request, 'manga_pages/create_chapter.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'id':id})
