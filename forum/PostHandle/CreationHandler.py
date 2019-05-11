# This class handles all forum/post creation

import datetime

from ..models import Discussion, Post, Category, DebateMode


# Creates a new Discussion
def create_discussion(title, descr, owner, categorie_id, mode):
    try:
        cat = Category.objects.get(key=categorie_id)
        deb_mode = DebateMode.objects.get(key=mode)
        Discussion.objects.create(title=title, descr=descr, owner=owner, category=cat, mode=deb_mode)
        return True
    except Exception as err:
        print(err)
        return False


# Creates a post in a Discussion
def create_post(owner, text, discussion_id):
    try:
        discussion = Discussion.objects.get(id=discussion_id)
        Post.objects.create(owner=owner, text=text, discussion=discussion, pub_date=datetime.datetime.now())
        return True
    except Exception as err:
        print(err)
        return True
