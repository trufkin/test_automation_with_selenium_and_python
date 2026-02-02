from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url='https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(url)
    treasure_chest = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#treasure")))
    valuex = treasure_chest.get_attribute("valuex")
    input_value = calc(valuex)
    input_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#answer")))
    robot_checkbox = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#robotCheckbox")))
    robots_rule_rdbtn = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#robotsRule")))
    submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    input_field.send_keys(input_value)
    robot_checkbox.click()
    robots_rule_rdbtn.click()
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
