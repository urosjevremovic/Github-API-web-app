import requests

from urllib import request as request_lib

from django.core.files.base import ContentFile


def user_data_by_username(username):
    """Takes user info from Github API and returns it."""

    url = 'https://api.github.com/users/{}'
    data = requests.get(url.format(username)).json()

    user_data = dict()
    user_data['username'] = data['login']
    avatar_url = data['avatar_url']
    try:
        response = request_lib.urlopen(avatar_url)
        user_data['avatar'] = ContentFile(response.read())
    except (TypeError, AttributeError):
        pass

    url_2 = url + '/repos'
    data = requests.get(url_2.format(username)).json()
    repos = []

    for each in data:
        repo_data = dict()
        repo_data['name'] = each['name']
        repo_data['language'] = each['language']
        repo_data['url'] = each['svn_url']
        repo_data['watchers_count'] = each['watchers_count']
        repo_data['description'] = each['description']
        repos.append(repo_data)

    return user_data, repos