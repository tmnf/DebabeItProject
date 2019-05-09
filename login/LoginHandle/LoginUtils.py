# This Class Handles User Authentication #

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from forum.models import ForumUser


# Logs User In
def LoginUser(username, password, request):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Sessão Iniciada Com Sucesso")
        return True
    else:
        return False


# Ends User Session
def Logout(request):
    try:
        logout(request)
        messages.success(request, "Sessão Terminada Com Sucesso")
        return True
    except:
        return False


# Register User Into Database
def RegisterUser(username, first_name, last_name, email, password, age, pic_url, request):
    try:
        us = User.objects.create_user(username, email, password)
        us.first_name = first_name
        us.last_name = last_name

        us.save()

        ForumUser.objects.create(user=us, user_age=age, user_pic=pic_url)

        messages.success(request, "Registado Com Sucesso")

        return True
    except:
        return False


# Storage User's Profile Picture
def UploadPicture(profile_pic):
    fs = FileSystemStorage()

    filename = fs.save(profile_pic.name, profile_pic)
    pic_url = fs.url(filename)

    return pic_url
