from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    first_name.send_keys("Vasea")
    last_name = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    last_name.send_keys("Pupkin")
    email = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    email.send_keys("a@a.com")
    phone = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    phone.send_keys("+180008000")
    address = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    address.send_keys("California")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()