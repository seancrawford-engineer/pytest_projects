from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_eninge_page(chrome_browser):
    chrome_browser.get('https://www.howacarworks.com/basics/the-engine')
    assert True