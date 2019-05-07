from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .LoginHandle.LoginUtils import RegisterUser, UploadPicture


# Create your views here.

def LoginPage(request):
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

        if RegisterUser(username, first_name, last_name, email, password, age, pic_url):
            return HttpResponseRedirect(reverse('forum_home'), {'register_sucess': "Registado com Sucesso"})

    return render(request, "login/RegisterPage.html");
