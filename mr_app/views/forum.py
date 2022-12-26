from django.shortcuts import render, redirect
from ..models import ForumPost, ForumPostComment
from django.contrib import messages
from django.http import HttpResponseRedirect

def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum.html', 
    {'user': request.user if request.user.is_authenticated else None,
    'posts':posts,})


def forum_post(request, id):
    post = ForumPost.objects.get(id=id)
    return render(request, 'forum/forum_post_details.html', 
    {'user': request.user if request.user.is_authenticated else None,
    'post':post, 
    'post_comments':post.forumpostcomment_set.all()})

def create_new_forum_post(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title != None and content != None:
        try:
            ForumPost.objects.create(title=title, content=content)
        except:
            messages.error(request=request, message="Este titulo já esta sendo utilizado em outra postagem!")

    else:
        messages.error(request=request, message="Preencha todos os campos!")
    return redirect(forum)




def add_comment_in_forum_post(request, id):
    content = request.POST.get('content')
    if content != None:
        try:
            forum_post = ForumPostComment(
                forumpost=ForumPost.objects.get(id=id),
                user=request.user if request.user.is_authenticated else None,
                content=content
                )
            forum_post.save()
        except Exception as ex:
            print(ex)
            messages.error(request=request, message="Este titulo já esta sendo utilizado em outra postagem!")

    else:
        messages.error(request=request, message="Preencha todos os campos!")

    
    return HttpResponseRedirect('/forum/'+str(id))



