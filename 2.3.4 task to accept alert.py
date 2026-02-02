import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL ='https://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(URL)
browser.maximize_window()
#What is ln(abs(12*sin(x))), where x = 915?
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    submit_button = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    submit_button.click()
    alert_popup = WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert_popup.accept()
    input_value = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value"))).text
    solution = str(math.log(abs(12*math.sin(int(input_value)))))
    answer_input_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#answer")))
    answer_input_field.send_keys(solution)
    solution_submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    solution_submit_button.click()
    task_answer = WebDriverWait(browser, 10).until(EC.alert_is_present()).text
    print(task_answer)
finally:
    time.sleep(10)
    browser.quit()