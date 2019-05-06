from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pic = models.ImageField(null=True, blank=True)
    user_age = models.CharField(max_length=100)

class Categorie(models.Model):
    categorie_title = models.CharField(max_length=100)

class Forum(models.Model):
    forum_title = models.CharField(max_length=100)
    forum_owner = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    forum_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    forum_mode = models.IntegerField()


class Post(models.Model):
    post_owner = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=5000)
    post_pub_date = models.DateTimeField("Data de publicação")
    post_forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    post_likes = models.IntegerField(default=0)
