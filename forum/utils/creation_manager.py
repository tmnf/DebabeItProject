# This class handles all forum/post creation

import datetime
import operator

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


# Checks if a user is signed up a DebateIt discussion
def check_if_signed(user, discussion):
    is_signed = check_if_exists(discussion.team1.all(), user) or check_if_exists(discussion.team2.all(), user)

    return is_signed


# Checks if a user exists in a team
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


# Checks if all requirements are fulfilled
def checks_requirements(request):
    form = request.POST
    error = False
    try:
        if form['title'] == '' or form['descr'] == '' or form['mode'] is None:
            error = 'Preencha todos os campos!'

        elif int(form['mode']) == constants.DEBATEIT_MODE and (form['option1'] == '' or form['option2'] == ''):
            error = 'Preencha as opções!'

    except Exception as err:
        print(err)
        error = 'Selecione um tipo de debate!'

    return error


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
        res.append(x)
        i += 1

    return res


# Retrieves top users
def get_top_users(users_list, max_users):
    aux = {}
    res = []

    for x in users_list:
        aux[x] = x.like_set.count()

    i = 0
    for key, value in sorted(aux.items(), key=operator.itemgetter(1), reverse=True):
        if i == max_users:
            break
        res.append(key)

    return res
