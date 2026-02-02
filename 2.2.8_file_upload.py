from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

urlka = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    browser.find_element(By.CSS_SELECTOR, "form>div>input:nth-child(2)").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "form>div>input:nth-child(4)").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "form>div>input:nth-child(6)").send_keys("a@a.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'new.txt')
    browser.find_element(By.CSS_SELECTOR, "input[id='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(3)
    browser.quit()
