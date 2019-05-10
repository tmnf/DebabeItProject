# This class handles all forum/post creation

import datetime

from ..models import Forum, Post, Categorie, DebateMode


# Creates a new Discussion
def create_forum(title, descr, owner, categorie_id, mode):
    try:
        cat = Categorie.objects.get(key=categorie_id)
        deb_mode = DebateMode.objects.get(key=mode)
        Forum.objects.create(title=title, descr=descr, owner=owner, categorie=cat, mode=deb_mode)
        return True
    except Exception as err:
        print(err)
        return False


# Creates a post in a Discussion
def create_post(owner, text, forum_id):
    try:
        forum = Forum.objects.get(id=forum_id)
        Post.objects.create(owner=owner, text=text, forum=forum, pub_date=datetime.datetime.now())
        return True
    except Exception as err:
        print(err)
        return True
