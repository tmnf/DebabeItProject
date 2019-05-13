from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True)
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


class DebateMode(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


class Discussion(models.Model):
    title = models.CharField(max_length=100)
    descr = models.TextField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mode = models.ForeignKey(DebateMode, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField("Data de publicação")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.discussion.title + " by: " + self.owner.username


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
