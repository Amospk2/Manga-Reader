import os
from django.utils.datastructures import MultiValueDictKeyError
from ..models import Manga, User, Capitulo, Page, Comment
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .utils import *

@login_required
def create_new_chapter(request, id):
    if request.user in Manga.objects.get(id=id).managers.all() or request.user.has_perm('mr_app.change_manga'):
        try:
            capitulo = Capitulo(
                manga=Manga.objects.get(id=7),
                title=request.POST.get('name'),
                release_date=request.POST.get('release_date'),
                description=request.POST.get('description'),
            )
            capitulo.save()

            for index, value in enumerate(request.FILES.getlist('images[]')):
                Page.objects.create(
                    capitulo=capitulo,
                    title=capitulo.title + "_" + str(index),
                    file=value
                )
        except MultiValueDictKeyError as ex:
            messages.error(request=request, message="Você deve escolhar uma imagem para o manga!")
            return render(create_chapter(request, id))
        except Exception as ex:
            print(ex)
            return HttpResponseRedirect('/manga/details/'+str(id))
        return HttpResponseRedirect('/manga/details/'+str(id))
    else:
        return HttpResponseRedirect('/')

@login_required
def create_chapter(request, id):
    users = User.objects.all()
    if request.user in Manga.objects.get(id=id).managers.all() or request.user.has_perm('mr_app.add_manga'):
        return render(request, 'manga_pages/create_chapter.html', {'user': check_if_has_user_activate(request), 'users':users, 'manga':Manga.objects.get(id=id)})
    return HttpResponseRedirect('/')
    

def view_chapter(request, capitulo):
    try:
        users = User.objects.all()
        pages = Capitulo.objects.get(id=capitulo).page_set.all()
    except Exception as ex:
        return HttpResponseRedirect('/')
    if(len(pages) == 0):
        return HttpResponseRedirect('/manga/details/' + str(Capitulo.objects.get(id=capitulo).manga.id))
    return render(request, 'manga_pages/view_chapter.html', \
        {'user': check_if_has_user_activate(request), 'users':users, 'pages':pages, \
        'page_info':{
        'capitulo':Capitulo.objects.get(id=capitulo),\
        'manga':Capitulo.objects.get(id=capitulo).manga, \
        'count_of_chapters':Capitulo.objects.get(id=capitulo).manga.capitulo_set.count(),
        'next':Capitulo.objects.get(id=capitulo).id + 1,
        'prev':Capitulo.objects.get(id=capitulo).id - 1,
        'comments':Capitulo.objects.get(id=capitulo).comment_set.all()
        }})

@login_required
def add_new_comment_for_chapter(request, id):
    try:
        comment = Comment(
            Capitulo=Capitulo.objects.get(id=id),
            user=check_if_has_user_activate(request),
            content = request.POST.get('content')
        )
        comment.save()
    except Exception as ex:
        messages.error(request=request, message="Os comentarios devem ter titulos unicos!")

    return HttpResponseRedirect('/manga/view-chapter/'+str(id))

def delete_chapter(request, id):
    cap = Capitulo.objects.get(id=id)
    manga = Capitulo.objects.get(id=id).manga_id
    cap.delete()
    return HttpResponseRedirect('/manga/details/'+str(manga))
    
    
    
