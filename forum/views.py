from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from login.LoginHandle.AuthUtils import CheckRespect
from .PostHandle.CreationHandler import create_discussion, create_post
from .Utils import constants
from .models import Discussion, Category, Post, Like


# Create your views here.

def MainPage(request):
    return render(request, "forum/MainPage.html")


def CategoriesPage(request):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, "forum/CategoriesPage.html", context)

def AboutPage(request):
    return render(request, "forum/AboutPage.html")


def CategoryDetails(request, category_id):
    logged_in = request.user.is_authenticated
    cat = Category.objects.get(key=category_id)

    context = {
        'logged_in': logged_in,
        'category': cat,
        'discussions': Discussion.objects.filter(category=cat)
    }

    return render(request, "forum/CategoryDetails.html", context)


def DiscussionDetails(request, discussion_id):
    if request.method == 'POST':
        success = create_post(request.user, request.POST['comment'], discussion_id)
        if success:
            return HttpResponseRedirect(reverse('forum_discussion', args=discussion_id))

    logged_in = request.user.is_authenticated
    discussion = Discussion.objects.get(id=discussion_id)

    context = {
        'logged_in': logged_in,
        'discussion': discussion,
        'posts': Post.objects.filter(discussion=discussion)
    }

    return render(request, "forum/DiscussionDetails.html", context)


@login_required
def AddDiscussion(request, category_id):

    if request.method == 'POST':
        form = request.POST
        success = create_discussion(form['title'], form['descr'], request.user, category_id, form['mode'])
        if success:
            return HttpResponseRedirect(reverse('forum_category', args=category_id))

    context = {
        'default': constants.DAFAULT_MODE,
        'debateIt': constants.DEBATEIT_MODE,
        'category_id': category_id
    }

    return render(request, 'forum/AddForum.html', context)


@login_required
def AtributeLike(request):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    user = post.owner

    if request.user != user:
        like, created = Like.objects.get_or_create(owner=user, post=post)

        if not created:
            like.delete()

        CheckRespect(user)

    return HttpResponseRedirect(reverse('forum_discussion', args=(post.discussion_id,)))
