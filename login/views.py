from django.shortcuts import render

# Create your views here.

def LoginPage(request):
    return render(request, "login/LoginPage.html")
