from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, include
from .LoginHandle.LoginUtils import RegisterUser
from .Forms import RegisterForm

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

        RegisterUser(username,first_name, last_name, email, password, age)

        return

    return render(request, "login/RegisterPage.html");