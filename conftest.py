import pytest

from config import Config


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
    return login_info.user_login


@pytest.fixture(scope='session')
def app_config(env, authentication_login):
    conf = Config(env)
    conf.token = authentication_login

    return conf
