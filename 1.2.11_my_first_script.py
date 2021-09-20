import time

# webdriver - it is a set of commands for controlling and manipulating browser
from selenium import webdriver

# This command initialize browser and you should see new browser window upon command execution
driver = webdriver.Chrome()

# Method 'get' tells browser to open website for the specified link
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# 'find_element_by_css_selector' method finds required element on the page by specified path to that element
# looking for the text input field
textarea = driver.find_element_by_css_selector(".textarea")

# Enter answer text to the located field
textarea.send_keys("get()")
time.sleep(5)

# Find a button that sends out the solution found
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Make driver click the button located
submit_button.click()
time.sleep(5)

# Close browser instance upon test completion
driver.quit()
