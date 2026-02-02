from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

try:
    link = "https://alphastagingtenant1.zenya-dev.nl/Login#/"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    userName = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#userNameField")))
    # userName = browser.find_element(By.CSS_SELECTOR, "#userNameField")
    # ActionChains(browser).pause(5).perform()
    userName.send_keys("xelag")

    userPassword = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#passwordField")))
    userPassword.send_keys("[eq,fkf321$%")

    submitButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#submitButton")))
    submitButton.click()


    ActionChains(browser).pause(5).perform()
    documentsPageUrl="https://alphastagingtenant1.zenya-dev.nl/iDocument/Default.aspx"
    browser.get(documentsPageUrl)

    searchSection = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#divobjAccordion_objSearchPane_PaneHeaderContainer")))
    searchSection.click()


    searchInput = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtSearchBox_SearchInput")))
    searchInput.send_keys("test")


    searchDocButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtSearchBox_SearchButton")))
    searchDocButton.click()

    # # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    #
    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    time.sleep(5)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()