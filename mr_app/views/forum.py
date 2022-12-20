from django.shortcuts import  render


def forum(request):
    return render(request, 'forum/forum.html')


def forum_post(request, id):
    return render(request, 'forum/forum_post_details.html')










