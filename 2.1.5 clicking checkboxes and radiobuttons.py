from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(url)
    varValue = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value")))
    x = varValue.text
    y = calc(x)
    answerField = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#answer")))
    answerField.send_keys(y)
    checkBox = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-check-label[for='robotCheckbox']")))
    checkBox.click()
    robotsRule = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".form-check-label[for='robotsRule']")))
    robotsRule.click()
    submitBtn = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".btn.btn-default")))
    submitBtn.click()
finally:
    time.sleep(10)
    browser.quit()