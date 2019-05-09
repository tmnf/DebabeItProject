from django.contrib import admin

from .models import ForumUser, Categorie, Post, Forum

# Register your models here.

admin.site.register(ForumUser)
admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Forum)
