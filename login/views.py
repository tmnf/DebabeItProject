from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from forum.Utils.MathUtils import GetAge
from .LoginHandle import LoginUtils


# User Authentication Page
def LoginPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('forum_home'))

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if username != '' and password != '':
            if LoginUtils.LoginUser(username, password, request):
                return HttpResponseRedirect(reverse('forum_home'))

    return render(request, "login/LoginPage.html")


# User Register Page
def RegisterPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('forum_home'))

    if request.method == "POST":

        username = request.POST["username"]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        age = request.POST['age']

        try:
            profile_pic = request.FILES['pic']
            pic_url = LoginUtils.UploadPicture(profile_pic)
        except:
            pic_url = None

        if LoginUtils.RegisterUser(username, first_name, last_name, email, password, age, pic_url, request):
            return HttpResponseRedirect(reverse('forum_home'))

    return render(request, "login/RegisterPage.html");


# Logs User Out
def logout(request):
    if request.user.is_authenticated:
        LoginUtils.Logout(request)
    return HttpResponseRedirect(reverse('forum_home'))


# User Profile Page
def profile(request):
    user = request.user

    if user.is_authenticated:
        context = {
            'user': user,
            'user_age': GetAge(user.forumuser.user_age)
        }
        return render(request, 'login/ProfilePage.html', context)

    return HttpResponseRedirect(reverse('forum_home'))
