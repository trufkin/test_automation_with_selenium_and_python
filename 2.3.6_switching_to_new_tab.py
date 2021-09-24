from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

urlka = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    browser.switch_to.window(browser.window_handles[1])
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(calc(input_value))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(5)
    browser.quit()
