from selenium import webdriver
from selenium.webdriver.common.by import By
import time

urlka = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(urlka)

    people_radiobutton = browser.find_element(By.CSS_SELECTOR, "input[id=peopleRule]")
    people_rbtn_status = people_radiobutton.get_attribute("checked")
    # print(people_rbtn_status)

    robots_radiobutton = browser.find_element(By.CSS_SELECTOR, "input[id=robotsRule]")
    robots_rbtn_status = robots_radiobutton.get_attribute("checked")
    # print(robots_rbtn_status)

    submit_button_status = browser.find_element(By.CSS_SELECTOR, "button.btn").get_attribute("disabled")
    print(submit_button_status)

    time.sleep(10)

    submit_button_status = browser.find_element(By.CSS_SELECTOR, "button.btn").get_attribute("disabled")
    print(submit_button_status)

finally:
    time.sleep(2)
    browser.quit()
