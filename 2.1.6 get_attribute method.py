from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    url = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(url)
    people_rdbtn = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-check-input#peopleRule")))
    people_checked = people_rdbtn.get_attribute("checked")
    assert people_checked is not None, "Error: People radio is NOT selected by default"
    # assert people_checked == "true", "Error: People radio is NOT selected by default"
finally:
    time.sleep(10)
    browser.quit()
