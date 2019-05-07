# This Class Handles User Authentication #

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from forum.models import ForumUser


def LoginUser(username, password, request):
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return True
    else:
        return False


def Logout(request):
    try:
        logout(request)
        return True
    except:
        return False

def RegisterUser(username, first_name, last_name, email, password, age, pic_url):
    try:
        us = User.objects.create_user(username, email, password)
        us.first_name = first_name
        us.last_name = last_name

        us.save()

        ForumUser.objects.create(user=us, user_age=age, user_pic=pic_url)

        return True
    except:
        return False


def UploadPicture(profile_pic):
    fs = FileSystemStorage()

    filename = fs.save(profile_pic.name, profile_pic)
    pic_url = fs.url(filename)

    return pic_url
