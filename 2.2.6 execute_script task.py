from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    url='https://suninjuly.github.io/execute_script.html'
    browser.get(url)
    browser.maximize_window()
    x_value = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value")))
    x_value_value = x_value.text
    input_value = calc(x_value_value)
    input_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#answer")))
    input_field.send_keys(input_value)
    robot_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#robotCheckbox")))
    robot_checkbox.click()
    robots_rule_element = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", robots_rule_element)
    robots_rule_rdbtn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#robotsRule")))
    robots_rule_rdbtn.click()
    submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    #input_field.send_keys(input_value)
    #robot_checkbox.click()
    #robots_rule_rdbtn.click()
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
