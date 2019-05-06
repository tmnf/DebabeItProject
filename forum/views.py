from django.shortcuts import render

# Create your views here.

def MainPage(request):
    return render(request, "forum/MainPage.html")

def CategoriesPage(request):
    return render(request, "forum/CategoriesPage.html")

def AboutPage(request):
    return render(request, "forum/AboutPage.html")


