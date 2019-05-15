from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from forum.utils.creation_manager import create_discussion, create_post, check_if_signed, generate_context
from login.login_manager.auth_utils import check_respect
from .models import Discussion, Category, Post, Like
from .utils import constants


# Main Page
def index(request):
    return render(request, "forum/MainPage.html")


# Categories Page
def categories_page(request):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, "forum/CategoriesPage.html", context)


# About Page
def about_page(request):
    return render(request, "forum/AboutPage.html")


# Category's Details
def category_details(request, category_id):
    logged_in = request.user.is_authenticated
    cat = Category.objects.get(key=category_id)

    context = {
        'logged_in': logged_in,
        'category': cat,
        'discussions': Discussion.objects.filter(category=cat)
    }

    return render(request, "forum/CategoryDetails.html", context)


# Detailed Discussion
def discussion_details(request, discussion_id):
    if request.method == 'POST':
        success = create_post(request.user, request.POST['comment'], discussion_id)
        if not success:
            return

    logged_in = request.user.is_authenticated
    discussion = Discussion.objects.get(id=discussion_id)

    if discussion.mode.key == constants.DEBATEIT_MODE:
        if logged_in:
            signed = check_if_signed(request.user, discussion)
            if not signed:
                context = generate_context(discussion, constants.NOT_SIGNED_PURP, logged_in)
                return render(request, "forum/DebateSignUp.html", context)

        context = generate_context(discussion, constants.DEBATEIT_PURP, logged_in)
        return render(request, "forum/DiscussionDetails.html", context)

    context = generate_context(discussion, constants.NORMAL_PURP, logged_in)
    return render(request, "forum/DiscussionDetails.html", context)


# Create Discussion Page
@login_required
def add_discussion(request, category_id):

    if request.method == 'POST':
        form = request.POST

        if int(form['mode']) == constants.DEBATEIT_MODE:
            success = create_discussion(form['title'], form['descr'], request.user, category_id,
                                        form['mode'], form['option1'], form['option2'])
        else:
            success = create_discussion(form['title'], form['descr'], request.user, category_id, form['mode'])

        if success:
            return HttpResponseRedirect(reverse('forum_category', args=category_id))

    context = {
        'default': constants.DAFAULT_MODE,
        'debateIt': constants.DEBATEIT_MODE,
        'category_id': category_id
    }

    return render(request, 'forum/AddForum.html', context)


# Like Input Handle
@login_required
def attribute_like(request):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    user = post.owner

    if request.user != user:
        like, created = Like.objects.get_or_create(owner=user, post=post)

        if not created:
            like.delete()

        check_respect(user)

    return HttpResponseRedirect(reverse('forum_discussion', args=(post.discussion_id,)))


# Debate SignUp Page
@login_required
def debate_signup(request):
    discussion = Discussion.objects.get(id=request.POST['disc'])
    option = int(request.POST['option'])

    if option == constants.FIRST_OPTION:
        discussion.team1.add(request.user)
    else:
        discussion.team2.add(request.user)

    return HttpResponseRedirect(reverse('forum_discussion', args=(discussion.id,)))
