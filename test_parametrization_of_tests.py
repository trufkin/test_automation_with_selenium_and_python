# 3.6.3 - Задание: параметризация тестов

from selenium import webdriver
import pytest
import time
import math

answer = math.log(int(time.time()))


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('my_variable', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_solve_the_problem(browser, my_variable):
    link = f"https://stepik.org/lesson/{my_variable}/step/1"
    browser.get(link)


