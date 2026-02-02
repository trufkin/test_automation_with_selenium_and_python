from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

urlka = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlka)
    summa = int(browser.find_element(By.CSS_SELECTOR, "#num1").text) + int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    select_dropdown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select_dropdown.select_by_value(str(summa))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(2)
    browser.quit()
