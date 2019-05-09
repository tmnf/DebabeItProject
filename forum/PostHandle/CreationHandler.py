# This class handles all forum/post creation

from ..models import Forum, Post


# Creates a new Discussion
def create_forum(title, descr, owner, categorie, mode):
    try:
        Forum.objects.create(title=title, descr=descr, owner=owner, categorie=categorie, mode=mode)
        return True
    except Exception as err:
        print(err)
        return False


# Creates a post in a Discussion
def create_post(owner, text, forum):
    try:
        Post.objects.create(owner=owner, text=text, forum=forum)
        return True
    except Exception as err:
        print(err)
        return True
