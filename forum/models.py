from django.contrib.auth.models import User
from django.db import models


# Respect Level of User
class ForumRespect(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


# Auxiliary user class
class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True)
    age = models.CharField(max_length=100)
    respect = models.ForeignKey(ForumRespect, on_delete=models.CASCADE, null=True, default=None)

    def set_respect(self, respect):
        self.respect = respect

    def __str__(self):
        return self.user.username


# Discussion Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


# Discussion Mode
class DebateMode(models.Model):
    title = models.CharField(max_length=100)
    key = models.IntegerField()

    def __str__(self):
        return self.title


# Discussion Option (Users can pick one of two sides)
class DebateOption(models.Model):
    title = models.CharField(max_length=50)
    key = models.IntegerField()

    def __str__(self):
        return self.title


# Discussion
class Discussion(models.Model):
    title = models.CharField(max_length=100)
    descr = models.TextField(default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    mode = models.ForeignKey(DebateMode, on_delete=models.CASCADE)

    options = models.ManyToManyField(DebateOption)
    team1 = models.ManyToManyField(User, related_name='team1', default=None)
    team2 = models.ManyToManyField(User, related_name='team2', default=None)

    def __str__(self):
        return self.title


# User Post
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField("Data de publicação")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.discussion.title + " by: " + self.owner.username


# Post/User Like
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
