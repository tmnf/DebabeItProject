from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404

from forum.utils import creation_manager
from login.login_manager.auth_utils import check_respect
from .models import Discussion, Category, Post, Like, User
from .utils import constants


# Main Page
def index(request):
    recent_discs = creation_manager.get_last_discussions(Discussion.objects.all().order_by('-id'), constants.MAX_DISCS)
    top_users = creation_manager.get_top_users(User.objects.all(), constants.MAX_USERS)

    context = {
        'recent_discs': recent_discs,
        'top_users': top_users,
        'active': 'home'
    }

    return render(request, "forum/MainPage.html", context)


# Categories Page
def categories_page(request):
    context = {
        'categories': Category.objects.all(),
        'active': 'categories'
    }

    return render(request, "forum/CategoriesPage.html", context)


# About Page
def about_page(request):
    context = {
        'email': constants.EMAIL,
        'phone1': constants.CELL_PHONE1,
        'phone2': constants.CELL_PHONE2,
        'active': 'about'
    }
    return render(request, "forum/AboutPage.html", context)


# Category's Details
def category_details(request, category_id):
    logged_in = request.user.is_authenticated
    cat = Category.objects.get(key=category_id)

    context = {
        'logged_in': logged_in,
        'category': cat,
        'discussions': Discussion.objects.filter(category=cat),
        'active': 'categories'
    }

    return render(request, "forum/CategoryDetails.html", context)


# Detailed Discussion
def discussion_details(request, discussion_id):
    if request.method == 'POST':
        if request.POST['comment'] != '':
            creation_manager.create_post(request.user, request.POST['comment'], discussion_id)
            return HttpResponseRedirect(reverse('forum_discussion', args=(discussion_id,)))

    logged_in = request.user.is_authenticated
    discussion = Discussion.objects.get(id=discussion_id)

    if discussion.mode.key == constants.DEBATEIT_MODE:
        if logged_in:
            signed = creation_manager.check_if_signed(request.user, discussion)
            if not signed:
                context = creation_manager.generate_context(discussion, constants.NOT_SIGNED_PURP, logged_in)
                return render(request, "forum/DebateSignUp.html", context)

        context = creation_manager.generate_context(discussion, constants.DEBATEIT_PURP, logged_in)
        return render(request, "forum/DiscussionDetails.html", context)

    context = creation_manager.generate_context(discussion, constants.NORMAL_PURP, logged_in)
    return render(request, "forum/DiscussionDetails.html", context)


# Create Discussion Page
@login_required
def add_discussion(request, category_id):
    error = False
    if request.method == 'POST':
        form = request.POST

        error = creation_manager.checks_requirements(request)

        if not error:
            if int(form['mode']) == constants.DEBATEIT_MODE:
                success = creation_manager.create_discussion(form['title'], form['descr'],
                                                             request.user, category_id, form['mode'],
                                                             form['option1'], form['option2'])
            else:
                success = creation_manager.create_discussion(form['title'], form['descr'],
                                                             request.user, category_id, form['mode'])

            if success:
                return HttpResponseRedirect(reverse('forum_category', args=category_id))

    context = {
        'default': constants.DAFAULT_MODE,
        'debateIt': constants.DEBATEIT_MODE,
        'category_id': category_id,
        'error': error,
    }

    return render(request, 'forum/AddDiscussion.html', context)


# Like Input Handle
@login_required
def attribute_like(request):
    post = get_object_or_404(Post, id=request.POST['post_id'])
    user = post.owner

    if request.user != user:
        like, created = Like.objects.get_or_create(owner=user, post=post, user=request.user)

        if not created:
            like.delete()

        check_respect(user)

    return HttpResponseRedirect(reverse('forum_discussion', args=(post.discussion_id,)))


# Debate SignUp Page
@login_required
def debate_signup(request):
    discussion = Discussion.objects.get(id=request.POST['disc'])

    try:
        option = int(request.POST['option'])

        if option == constants.FIRST_OPTION:
            discussion.team1.add(request.user)
        else:
            discussion.team2.add(request.user)
    except Exception as err:
        print(err)

    return HttpResponseRedirect(reverse('forum_discussion', args=(discussion.id,)))
