from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

urlka = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(input_value))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(3)
    browser.quit()