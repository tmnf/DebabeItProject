from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from forum.Utils.MathUtils import GetAge
from .LoginHandle import LoginUtils


# Create your views here.

def LoginPage(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        if username != '' and password != '':
            if LoginUtils.LoginUser(username, password, request):
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
            pic_url = LoginUtils.UploadPicture(profile_pic)
        except:
            pic_url = None

        if LoginUtils.RegisterUser(username, first_name, last_name, email, password, age, pic_url, request):
            return HttpResponseRedirect(reverse('forum_home'))

    return render(request, "login/RegisterPage.html");


def logout(request):
    if LoginUtils.Logout(request):
        return HttpResponseRedirect(reverse('forum_home'))


def profile(request):
    user = request.user

    context = {
        'user': user,
        'user_age': GetAge(user.forumuser.user_age)
    }

    if user.is_authenticated:
        return render(request, 'login/ProfilePage.html', context)

    return render(request, 'forum/MainPage.html')
