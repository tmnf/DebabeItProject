from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^register/$', views.register_page, name='register_page'),

    url(r'^profile/$', views.profile, name='profile_page'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile_page_ext')
]
