from django.urls import path
from login import views

urlpatterns = [
    path('login/', views.LoginPage, name='login_page'),
    path('register/', views.RegisterPage, name='register_page'),
]