from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math

def function_from_x(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    url = 'https://suninjuly.github.io/execute_script.html'
    browser.get(url)
    x = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#input_value')))


finally:
    browser.quit()