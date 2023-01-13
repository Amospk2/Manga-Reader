from django.shortcuts import render, redirect
from ..models import ForumPost, ForumPostComment
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .utils import *

def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum.html', 
    {'user': check_if_has_user_activate(request),
    'posts':posts,})

def forum_post(request, id):
    post = ForumPost.objects.get(id=id)
    return render(request, 'forum/forum_post_details.html', 
    {'user': check_if_has_user_activate(request),
    'post':post, 
    'post_comments':post.forumpostcomment_set.all()})

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def add_comment_in_forum_post(request, id):
    content = request.POST.get('content')
    if content != None:
        try:
            forum_post = ForumPostComment(
                forumpost=ForumPost.objects.get(id=id),
                user=check_if_has_user_activate(request),
                content=content
                )
            forum_post.save()
        except Exception as ex:
            print(ex)
            messages.error(request=request, message="Este titulo já esta sendo utilizado em outra postagem!")
    else:
        messages.error(request=request, message="Preencha todos os campos!")
    
    return HttpResponseRedirect('/forum/'+str(id))

@login_required(login_url='/login')
def remove_forum_post(request, id):
    ForumPost.objects.filter(id=id).delete()

    return redirect(forum)

@login_required(login_url='/login')
def remove_comment_in_forum_post(request, id):
    forum_post_comment = ForumPostComment.objects.get(id=id)

    forum_post_id = forum_post_comment.forumpost.id

    forum_post_comment.delete()

    return HttpResponseRedirect('/forum/' + str(forum_post_id))