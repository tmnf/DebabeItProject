from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.LoginPage, name='login_home'),
    path('register/', views.RegisterPage, name='register_home'),
]