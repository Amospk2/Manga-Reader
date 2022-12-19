from django.shortcuts import render


def manga(request):
    return render(request, 'manga_pages/mangas.html', {'user': request.user if request.user.is_authenticated else None})
