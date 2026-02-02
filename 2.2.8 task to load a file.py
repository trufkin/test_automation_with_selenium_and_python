import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL ='https://suninjuly.github.io/file_input.html'
file_directory = 'C:\\Users\\alexander.trufkin.ADDCODE\\Downloads'
file_name = 'file.txt'
browser = webdriver.Chrome()
browser.get(URL)
browser.maximize_window()

try:
    first_name_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='firstname']")))
    last_name_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='lastname']")))
    email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
    upload_file_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#file")))
    submit_button = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    file_path = os.path.join(file_directory, file_name)
    first_name_input.send_keys("Alex")
    last_name_input.send_keys("Xela")
    email_input.send_keys("a@a.com")
    upload_file_button.send_keys(file_path)
    submit_button.click()
    alert_popup = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_text = alert_popup.text
    magic_number = alert_text.split(":", 1)[1].strip()
    print(magic_number)
finally:
    time.sleep(10)
    browser.quit()