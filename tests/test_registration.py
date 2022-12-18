from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from selenium.webdriver.chrome.options import Options


def test_registration_correct_values_registration_success():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/notan/Sprint_3/chromedriver.exe')
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys('Anton')
    driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys('anton_monogarov_05_305@yandex.ru')
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD_INPUT).send_keys('225577')
    driver.find_element(*TestLocators.REGISTRATION_CONFIRM).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_ENTER))
    assert driver.find_element(*TestLocators.HEADER_ENTER).text == 'Вход'
    driver.quit()


def test_registration_incorrect_values_registration_failed():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/notan/Sprint_3/chromedriver.exe')
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_MAIN).click()
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
    driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys('Anton')
    driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys('anton_monogarov_05_245@yandex.ru')
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD_INPUT).send_keys('22557')
    driver.find_element(*TestLocators.REGISTRATION_CONFIRM).click()
    assert driver.find_element(*TestLocators.REGISTRATION_INCORRECT_PASSWORD).text == "Некорректный пароль"
    driver.quit()
