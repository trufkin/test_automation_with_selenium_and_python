from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

urlka = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    answer = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer)
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.CSS_SELECTOR, "button.btn"))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(3)
    browser.quit()


