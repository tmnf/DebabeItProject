from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .PostHandle.CreationHandler import create_forum, create_post
from .Utils import constants


# Create your views here.

def MainPage(request):
    return render(request, "forum/MainPage.html")

def CategoriesPage(request):
    return render(request, "forum/CategoriesPage.html")

def AboutPage(request):
    return render(request, "forum/AboutPage.html")


def AddForum(request, categorie_id):
    if request.method == 'POST':
        form = request.POST
        success = create_forum(form['title'], form['descr'], request.user, categorie_id, form['mode'])
        if success:
            return HttpResponseRedirect(reverse('forum_home'))

    context = {
        'default': constants.DAFAULT_MODE,
        'debateIt': constants.DEBATEIT_MODE,
        'categorie': categorie_id
    }

    return render(request, 'forum/AddForum.html', context)


def AddPost(request, forum_id):
    if request.method == 'POST':
        success = create_post(request.user, request.POST['comment'], forum_id)
        if success:
            return HttpResponseRedirect(reverse('forum_home'))

    context = {
        'forum_id': forum_id
    }
    return render(request, 'forum/AddPost.html', context)
