from pytest import fixture

from config import Config

def pytest_addoption(parser):
    parser.addoption("--env",action="store",help="Environment to run tests against")

@fixture(scope='function')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='function')
def app_config(env):
    cfg = Config(env)
    return cfg

    