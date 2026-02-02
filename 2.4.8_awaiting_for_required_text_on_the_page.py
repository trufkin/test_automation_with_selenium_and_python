from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

urlka = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "#book.btn").click()
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    answer_value = calc(input_value)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(answer_value)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    time.sleep(5)
    browser.quit()
