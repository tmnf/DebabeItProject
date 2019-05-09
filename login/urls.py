from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^login/', views.LoginPage, name='login_page'),
    url(r'^register/', views.RegisterPage, name='register_page'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^profile/', views.profile, name='profile_page'),
]