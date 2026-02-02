import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



URL ='https://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(URL)
browser.maximize_window()
#What is ln(abs(12*sin(x))), where x = 915?
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    before_window_handles = len(browser.window_handles)
    submit_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.trollface.btn.btn-primary")))
    submit_button.click()
    WebDriverWait(browser, 10).until(lambda d: len(browser.window_handles) > before_window_handles)
    browser.switch_to.window(browser.window_handles[1])
    input_value = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input_value"))).text
    solution = calc(input_value)
    answer_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#answer")))
    answer_field.send_keys(solution)
    submit_solution_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    submit_solution_button.click()
    task_answer = WebDriverWait(browser, 10).until(EC.alert_is_present()).text.split(':', 1)[1]
    print(task_answer.strip())
finally:
    time.sleep(10)
    browser.quit()