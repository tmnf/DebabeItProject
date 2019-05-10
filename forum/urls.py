from django.conf.urls import url

from forum import views

urlpatterns = [
    url(r'^$', views.MainPage, name='forum_home'),
    url(r'^categories/', views.CategoriesPage, name='forum_categories'),
    url(r'^about/', views.AboutPage, name='forum_about'),
    url(r'^add/(?P<categorie_id>[0-9]+)/$', views.AddForum, name='forum_add')
]