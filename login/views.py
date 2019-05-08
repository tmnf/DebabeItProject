from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .LoginHandle.LoginUtils import RegisterUser, UploadPicture, LoginUser, Logout


# Create your views here.

def LoginPage(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if username != '' and password != '':
            if LoginUser(username, password, request):
                return HttpResponseRedirect(reverse('forum_home'))

    return render(request, "login/LoginPage.html")

def RegisterPage(request):
    if request.method == "POST":

        username = request.POST["username"]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        age = request.POST['age']

        try:
            profile_pic = request.FILES['pic']
            pic_url = UploadPicture(profile_pic)
        except:
            pic_url = None

        if RegisterUser(username, first_name, last_name, email, password, age, pic_url, request):
            return HttpResponseRedirect(reverse('forum_home'))

    return render(request, "login/RegisterPage.html");


def logout(request):
    if Logout(request):
        return HttpResponseRedirect(reverse('forum_home'))
