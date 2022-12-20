from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    tipo = models.CharField(max_length=30, unique=False, blank=True)
    data_nascimento = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Manga(models.Model):
    title = models.CharField(max_length=30, unique=True, blank=False)
    release_date = models.DateField()
    author = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField()
    tags = models.TextField()
    image = models.ImageField(default=None)
    managers = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    
class Capitulo(models.Model):
    fk_manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    release_date = models.DateField()
    title = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField()
    

    def __str__(self):
        return self.title

class Page(models.Model):
    fk_capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True, blank=False)
    file = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    fk_page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, unique=True, blank=False)
    content = models.TextField()

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ForumPostComment(models.Model):
    fk_forumpost = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
