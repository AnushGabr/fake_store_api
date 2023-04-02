import pytest
import requests
from config import Config
import json


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="url",
        help="Environment to run tests against"
    )


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def authentication_login(env):
    login_info = Config(env)
    login_info_dict = login_info.user_login
    access_token_text = requests.post('https://fakestoreapi.com/auth/login', login_info_dict).text
    access_token_json = json.loads(access_token_text)

    return access_token_json['token']


@pytest.fixture(scope='session')
def app_config(env, authentication_login):
    conf = Config(env)
    conf.token = authentication_login

    return conf
