import requests

# Exposing the session allows Betamax to spy on requests
# made to the github API.

session = requests.Session()


def list_repos(username):
    url = 'https://api.github.com/users/{}/repos'.format(username)
    res = session.get(url)
    return res.json()
