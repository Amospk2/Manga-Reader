from django.utils.datastructures import MultiValueDictKeyError
from ..models import Manga, User, Capitulo, Page, Comment
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required(perm='mr_app.add_capitulo', raise_exception=True)
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

@login_required
@permission_required(perm='mr_app.add_capitulo', raise_exception=True)
def create_chapter(request, id):
    users = User.objects.all()
    return render(request, 'manga_pages/create_chapter.html', {'user': request.user if request.user.is_authenticated else None, 'users':users, 'id':id})

def view_chapter(request, capitulo):
    try:
        users = User.objects.all()
        pages = Capitulo.objects.get(id=capitulo).page_set.all()
    except Exception as ex:
        return HttpResponseRedirect('/')
    if(len(pages) == 0):
        return HttpResponseRedirect('/manga/details/' + str(Capitulo.objects.get(id=capitulo).manga.id))
    return render(request, 'manga_pages/view_chapter.html', \
        {'user': request.user if request.user.is_authenticated else None, 'users':users, 'pages':pages, \
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
        print(id)
        comment = Comment(
            Capitulo=Capitulo.objects.get(id=id),
            user=request.user if request.user.is_authenticated else None,
            content = request.POST.get('content')
        )
        comment.save()
    except Exception as ex:
        messages.error(request=request, message="Os comentarios devem ter titulos unicos!")

    return HttpResponseRedirect('/manga/view-chapter/'+str(id))