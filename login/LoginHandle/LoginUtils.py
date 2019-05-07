# This Class Handles User Authentication #

from django.contrib.auth.models import User
from forum.models import ForumUser

def RegisterUser(username, first_name, last_name, email, password, age):

    us = User.objects.create_user(username,email,password)
    us.first_name =first_name
    us.last_name= last_name

    us.save()

    ForumUser.objects.create(user=us, user_age=age)
