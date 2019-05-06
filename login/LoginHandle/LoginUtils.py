# This Class Handles User Authentication #

from django.contrib.auth.models import User
from forum.models import ForumUser

def RegisterUser(username, first_name, last_name, email, age, password):

    try:
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        ForumUser.objects.create(user=user, user_age=age)

        return True
    except:
        return False
