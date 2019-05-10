# This class handles all forum/post creation

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
def create_post(owner, text, forum):
    try:
        Post.objects.create(owner=owner, text=text, forum=forum)
        return True
    except Exception as err:
        print(err)
        return True
