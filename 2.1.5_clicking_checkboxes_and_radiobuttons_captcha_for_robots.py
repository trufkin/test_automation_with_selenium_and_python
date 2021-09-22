from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# prerequisites:
urlka = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(urlka)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    answer = calc(x)

    answer_field = browser.find_element(By.CSS_SELECTOR, "input[id=answer]")
    answer_field.send_keys(answer)
    time.sleep(2)

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "input[id=robotCheckbox]")
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]")
    robot_radiobutton.click()
finally:
    time.sleep(2)
    browser.quit()



