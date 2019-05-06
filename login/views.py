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
        form = RegisterForm(request.POST)

        username = form.cleaned_data["username"]
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        age = form.cleaned_data['age']

        print(username, first_name, last_name, email, password, age)

        if RegisterUser(username, first_name, last_name, email, age, password):
            return include("forum.urls")

    return render(request, "login/RegisterPage.html");