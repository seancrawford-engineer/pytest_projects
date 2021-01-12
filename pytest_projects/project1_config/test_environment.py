from pytest import mark

def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80
    
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080
   
@mark.skip(reason="Testing the skip feature of pytest")
def test_this_needs_work():
    assert False
    
@mark.xfail(reason="This feature should have been deprecated")
def test_this_should_always_fail():
    assert False