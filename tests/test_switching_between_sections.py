from locators import TestLocators
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_switching_to_sauces_from_rolls_success():
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
    driver.find_element(*TestLocators.SAUCES).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.SAUCE_TRADITIONAL_GALACTIC))
    assert driver.find_element(*TestLocators.SAUCE_TRADITIONAL_GALACTIC).text == "Соус традиционный галактический"
    driver.quit()


def test_switching_to_fillings_from_rolls_success():
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
    driver.find_element(*TestLocators.FILLINGS).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.MARTIAN_MAGNOLIA_BIO_CUTLET))
    assert driver.find_element(*TestLocators.MARTIAN_MAGNOLIA_BIO_CUTLET).text == "Биокотлета из марсианской Магнолии"
    driver.quit()


def test_switching_to_rolls_from_sauces_success():
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
    driver.find_element(*TestLocators.SAUCES).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.SAUCE_TRADITIONAL_GALACTIC))
    driver.find_element(*TestLocators.ROLLS).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.FLUORESCENT_BUN))
    assert driver.find_element(*TestLocators.FLUORESCENT_BUN).text == "Флюоресцентная булка R2-D3"
