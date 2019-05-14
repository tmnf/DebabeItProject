from django.conf.urls import url

from forum import views

urlpatterns = [
    url(r'^$', views.MainPage, name='forum_home'),
    url(r'^about/', views.AboutPage, name='forum_about'),

    url(r'^categories/', views.CategoriesPage, name='forum_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.CategoryDetails, name='forum_category'),
    url(r'^category/(?P<category_id>[0-9]+)/add/$', views.AddDiscussion, name='forum_add'),

    url(r'^discussion/(?P<discussion_id>[0-9]+)/$', views.DiscussionDetails, name='forum_discussion'),

    url(r'^like/$', views.AtributeLike, name='forum_like'),
]