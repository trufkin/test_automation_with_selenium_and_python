from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    url = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(url)
    number1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#num1"))).text
    number2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#num2"))).text
    summa = str(int(number1) + int(number2))
    #cssSelector = "\"[value='"+summa+"']\""
    #print(cssSelector)
    dropdown = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#dropdown")))
    dropdown.click()
    correct_answer = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[value='"+summa+"']")))
    correct_answer.click()
    submit_btn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-default")))
    submit_btn.click()
finally:
    time.sleep(10)
    browser.quit()

