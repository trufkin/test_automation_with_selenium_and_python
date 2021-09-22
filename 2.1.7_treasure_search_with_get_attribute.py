from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

urlka = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    time.sleep(2)
    valuex_from_treasure = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    answer = calc(valuex_from_treasure)
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "input[id=robotCheckbox]").click()
    browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(5)
    browser.quit()
