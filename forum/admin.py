from django.contrib import admin

from .models import ForumUser, Category, Post, Discussion, DebateMode, Like, ForumRespect

# Models displayed in admin page

admin.site.register(ForumUser)
admin.site.register(Category)
admin.site.register(DebateMode)
admin.site.register(Post)
admin.site.register(Discussion)
admin.site.register(Like)
admin.site.register(ForumRespect)
