from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    url = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(url)
    #browser.execute_script("alert('Hello!!!')")
    #browser.execute_script("document.title='Script executing';")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    time.sleep(10)
    browser.quit()
