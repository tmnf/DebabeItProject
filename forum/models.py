from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True)
    age = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Categorie(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.categorie_title


class DebateMode(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


class Forum(models.Model):
    title = models.CharField(max_length=100)
    descr = models.TextField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    mode = models.ForeignKey(DebateMode, on_delete=models.CASCADE)

    def __str__(self):
        return self.forum_title


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField("Data de publicação")
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_forum.forum_title + " by: " + self.post_owner.user.username
