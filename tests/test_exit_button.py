from locators import TestLocators
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_exit_button_from_personal_area_success():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/notan/Sprint_3/chromedriver.exe')
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_MAIN).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_EMAIL_INPUT))
    driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys('anton_monogarov_05_225@yandex.ru')
    driver.find_element(*TestLocators.REGISTRATION_PASSWORD_INPUT).send_keys('225577')
    driver.find_element(*TestLocators.LOG_IN_BUTTON_CONFIRM).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
    driver.find_element(*TestLocators.PERSONAL_AREA_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_PROFILE_INFORMATION))
    driver.find_element(*TestLocators.EXIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOG_IN_BUTTON_CONFIRM))
    assert driver.find_element(*TestLocators.LOG_IN_BUTTON_CONFIRM).text == "Войти"
    driver.quit()
