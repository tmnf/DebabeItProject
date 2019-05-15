# This class handles all forum/post creation

import datetime

from forum.models import Discussion, Post, Category, DebateMode, DebateOption
from forum.utils import constants


# Creates a new Discussion
def create_discussion(title, descr, owner, categorie_id, mode, option1=None, option2=None):
    try:
        cat = Category.objects.get(key=categorie_id)
        deb_mode = DebateMode.objects.get(key=mode)
        discussion = Discussion.objects.create(title=title, descr=descr, owner=owner, category=cat, mode=deb_mode)

        if int(mode) == constants.DEBATEIT_MODE:
            op1 = DebateOption.objects.create(title=option1, key=constants.FIRST_OPTION)
            op2 = DebateOption.objects.create(title=option2, key=constants.SECOND_OPTION)
            discussion.options.add(op1)
            discussion.options.add(op2)

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


# Checks if a user is signed in a DebateIt discussion
def check_if_signed(user, discussion):
    is_signed = check_if_exists(discussion.team1.all(), user) or check_if_exists(discussion.team2.all(), user)

    return is_signed


def check_if_exists(team, user):
    for x in team:
        if x.id == user.id:
            return True
    return False


# Generates a context to display on Discussion Details
def generate_context(discussion, purpose, logged_in):
    context = {'discussion': discussion, 'logged_in': logged_in}

    if purpose == constants.NOT_SIGNED_PURP:
        context = {**context, 'options': discussion.options.all()}

    elif purpose == constants.NORMAL_PURP:
        context = {**context, 'posts': Post.objects.filter(discussion=discussion)}

    elif purpose == constants.DEBATEIT_PURP:
        team1_likes = get_like_count(discussion.team1.all(), discussion)
        team2_likes = get_like_count(discussion.team2.all(), discussion)

        context = {
            **context,
            'options': discussion.options.all(),
            'posts': Post.objects.filter(discussion=discussion),
            'team1_likes': team1_likes,
            'team2_likes': team2_likes,
            'debate': True
        }

    return context


# Counts how many likes a team has in a DebateIt discussion
def get_like_count(team, discussion):
    aux = 0
    for x in team:
        for y in x.post_set.filter(discussion=discussion):
            aux += y.like_set.count()
    return aux


# Retrieves last discussions
def get_last_discussions(discussion_list, max_discussions):
    res = []

    i = 0
    for x in discussion_list:
        if i == max_discussions:
            break
        res[i] = x
        i += 1

    return res


# Retrieves top users
def get_top_users(users_list, max_user):
    res = []

    i = 0
    for x in users_list:
        if i == max_user:
            break
        res[i] = x
        i += 1

    return res

    return 10
