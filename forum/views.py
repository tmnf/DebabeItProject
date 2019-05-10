from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .PostHandle.CreationHandler import create_forum
from .Utils import constants


# Create your views here.

def MainPage(request):
    return render(request, "forum/MainPage.html")

def CategoriesPage(request):
    return render(request, "forum/CategoriesPage.html")

def AboutPage(request):
    return render(request, "forum/AboutPage.html")


def AddForum(request, categorie):
    if request.method == 'POST':
        form = request.POST
        success = create_forum(form['title'], form['descr'], request.user, categorie, form['mode'])
        if success:
            return HttpResponseRedirect(reverse('forum_home'))

    context = {
        'default': constants.DAFAULT_MODE,
        'debateIt': constants.DEBATEIT_MODE,
        'categorie': categorie
    }

    return render(request, 'forum/AddForum.html', context)
