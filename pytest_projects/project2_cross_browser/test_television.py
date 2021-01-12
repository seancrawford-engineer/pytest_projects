from pytest import mark


def test_television_turns_on(tv_brand):
    #first_brand = tv_brand[0]
    #print ("hello TV Land")
    x = slice(1,4,2)
    print(f"{tv_brand[x]} turns on as expected")
    #print(f"{tv_brand} turns on as expected")

@mark.skip
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('https://techstepacademy.com/training-ground')
    