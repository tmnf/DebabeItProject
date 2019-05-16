from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from forum.utils.math_utils import get_age
from .login_manager import auth_utils


# User Authentication Page
def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('forum_home'))

    error = False
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if username != '' and password != '':
            if auth_utils.login_user(username, password, request):
                return HttpResponseRedirect(reverse('forum_home'))
            else:
                error = "Informações inválidas ou o utilizador não existe"
        else:
            error = "Preencha todos os campos!"

    context = {
        'error': error
    }

    return render(request, "login/LoginPage.html", context)


# User Register Page
def register_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('forum_home'))

    error = False
    if request.method == "POST":

        username = request.POST["username"]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        age = request.POST['age']

        try:
            profile_pic = request.FILES['pic']
            pic_url = auth_utils.upload_picture(profile_pic)
        except Exception as err:
            print(err)
            pic_url = None

        if auth_utils.register_user(username, first_name, last_name, email, password, age, pic_url, request):
            return HttpResponseRedirect(reverse('forum_home'))
        else:
            error = "Campos em falta, inválidos ou utilizador já existe"

    context = {
        'error': error
    }

    return render(request, "login/RegisterPage.html", context)


# Logs User Out
@login_required
def logout_user(request):
    auth_utils.logout_user(request)
    return HttpResponseRedirect(reverse('forum_home'))


# User's Profile Page
def profile(request, user_id=None):
    if user_id is None:
        user = request.user
    else:
        user = User.objects.get(id=user_id)

    context = {
        'user': user,
        'user_age': get_age(user.forumuser.age)
    }

    return render(request, 'login/ProfilePage.html', context)
