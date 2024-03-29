# 3.4.2 - Классические фикстуры (fixtures)

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


# создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта
class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("Class #1 >> test #1")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("Class #1 >> test #2")
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestIntermediate():
    def test_intermediate(self):
        print("***************************************************")

# создание браузера для каждого теста во втором тест-сьюте
class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("Class #2 >> test #1")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("Class #2 >> test #2")
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
