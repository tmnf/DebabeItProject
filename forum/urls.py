from django.conf.urls import url

from forum import views

urlpatterns = [
    url(r'^$', views.index, name='forum_home'),
    url(r'^about/', views.about_page, name='forum_about'),

    url(r'^categories/', views.categories_page, name='forum_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category_details, name='forum_category'),
    url(r'^category/(?P<category_id>[0-9]+)/add/$', views.add_discussion, name='forum_add'),

    url(r'^discussion/(?P<discussion_id>[0-9]+)/$', views.discussion_details, name='forum_discussion'),

    url(r'^like/$', views.attribute_like, name='forum_like'),
    url(r'^debate/sign/$', views.debate_signup, name='forum_signup'),
]
