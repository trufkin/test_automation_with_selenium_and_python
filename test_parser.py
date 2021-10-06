# 3.6.6 - Conftest.py и передача параметров в командной строке
import time
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)
    browser.find_element_by_css_selector("#login_link")