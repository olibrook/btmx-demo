import betamax

import btmx.github_client as github_client
import btmx.views as views


with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'btmx-demo/test/cassettes'


def test_list_repos():
    with betamax.Betamax(github_client.session) as vcr:
        vcr.use_cassette('test_list_repos')
        views.list_repos()


def test_list_repos_two():
    with betamax.Betamax(github_client.session) as vcr:
        vcr.use_cassette('test_list_repos_two')
        views.list_repos()
