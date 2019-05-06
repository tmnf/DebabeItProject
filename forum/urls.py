from django.urls import path, include
from forum import views

urlpatterns = [
    path('', views.MainPage, name='forum_home'),
    path('categories/', views.CategoriesPage, name='forum_categories'),
    path('about/', views.AboutPage, name='forum_about'),
    path('login/', include("login.urls"))
]