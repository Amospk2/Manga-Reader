from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    type = models.CharField(max_length=30, unique=False, blank=True)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

class Manga(models.Model):
    title = models.CharField(max_length=30, unique=True, blank=False)
    release_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    tags = models.TextField()
    image = models.ImageField(upload_to='manga/',default=None)
    managers = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    
class Capitulo(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField()
    

    def __str__(self):
        return self.title

class Page(models.Model):
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True, blank=False)
    file = models.ImageField(upload_to='page/',)

    def __str__(self):  
        return self.title


class Comment(models.Model):
    Capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)


class ForumPost(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ForumPostComment(models.Model):
    forumpost = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    content = models.TextField()
    publish_date = models.DateField(default=timezone.now)
