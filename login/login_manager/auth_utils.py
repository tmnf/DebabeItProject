# This Class Handles User Authentication #

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from forum.models import ForumUser, ForumRespect
from forum.utils import constants


# Logs User In
def login_user(username, password, request):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Sessão Iniciada Com Sucesso")
        return True
    else:
        return False


# Ends User Session
def logout_user(request):
    try:
        logout(request)
        messages.success(request, "Sessão Terminada Com Sucesso")
        return True
    except Exception as error:
        print(error)
        return False


# Register User Into Database
def register_user(username, first_name, last_name, email, password, age, pic_url, request):
    try:
        us = User.objects.create_user(username, email, password)
        us.first_name = first_name
        us.last_name = last_name

        us.save()

        respect_lvl = ForumRespect.objects.get(key=constants.NOVATO)

        ForumUser.objects.create(user=us, age=age, pic=pic_url, respect=respect_lvl)

        messages.success(request, "Registado Com Sucesso")

        return True
    except Exception as error:
        print(error)
        return False


# Storage User's Profile Picture
def upload_picture(profile_pic):
    fs = FileSystemStorage()

    filename = fs.save(profile_pic.name, profile_pic)
    pic_url = fs.url(filename)

    return pic_url


# Checks and Updates User Respect
def check_respect(user):
    likes = user.like_set.count()

    key = constants.NOVATO

    if likes >= constants.DITADOR_MIN:
        key = constants.DITADOR
    elif likes >= constants.VITORIOSO_MIN:
        key = constants.VITORIOSO
    elif likes >= constants.DEBATENTE_MIN:
        key = constants.DEBATENTE
    elif likes >= constants.AMADOR_MIN:
        key = constants.AMADOR
    elif likes >= constants.ENTUSIASTA_MIN:
        key = constants.ENTUSIASTA

    respect_lvl = ForumRespect.objects.get(key=key)

    user.forumuser.set_respect(respect_lvl)
    user.forumuser.save()
