from selenium.webdriver.common.by import By


class TestLocators:

    REGISTRATION_BUTTON = By.XPATH, '//*[@href = "/register"]' #кнопка зарегистрироваться
    REGISTRATION_CONFIRM = By.XPATH, '//*[text() = "Зарегистрироваться"]' #кнопка подтверждения регистрации
    REGISTRATION_NAME_INPUT = By.XPATH, 'html/body/div/div/main/div/form/fieldset[1]/div/div/input' #поле ввода имени при регистрации
    REGISTRATION_EMAIL_INPUT = By.XPATH, 'html/body/div/div/main/div/form/fieldset[2]/div/div/input' #поле ввода email при регистрации
    REGISTRATION_PASSWORD_INPUT = By.XPATH, '//*[@type = "password"]' #поле ввода пароля при регистрации
    LOG_IN_BUTTON_MAIN = By.XPATH, '//*[text() = "Войти в аккаунт"]'  # кнопка "войти в аккаунт" на главной странице
    LOG_IN_BUTTON_CONFIRM = By.XPATH, '//*[text() = "Войти"]'  # кнопка войти на странице ввода данных
    LOGIN_EMAIL_INPUT = By.XPATH, 'html/body/div/div/main/div/form/fieldset/div/div/input' #поле ввода email при входе
    PERSONAL_AREA_BUTTON = By.XPATH, '//*[contains(text(), "Личный Кабинет")]' # кнопка "личный кабинет" на главной странице
    LOG_IN_BUTTON_FROM_REGISTRATION_FORM = By.XPATH, '//*[@href = "/login"]' #кнопка "Войти" из формы регистрации
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//*[@href = "/forgot-password"]'  # кнопка "Восстановить пароль"
    LOG_IN_BUTTON_FROM_PASSWORD_RECOVERY_FORM = By.XPATH, '//*[@href = "/login"]' #кнопка "Войти" из формы восстановления пароля
    REGISTRATION_INCORRECT_PASSWORD = By.XPATH, '//*[contains(@class, "input__error")]' #сообщение "Некорректный пароль" при регистрации
    HEADER_ENTER = By.XPATH, '//*[text() = "Вход"]' #заголовок "Вход" на странице с вводом email и пароля для входа
    MAKE_ORDER_BUTTON = By.XPATH, '//*[contains(text(), "Оформить заказ")]' #кнопка "Оформить заказ"
    ACCOUNT_PROFILE_INFORMATION = By.XPATH, '//*[@href = "/account/profile"]' #информация о данных аккаунта в личном кабинете
    CONSTRUCTOR_BUTTON = By.XPATH, '//*[contains(text(), "Конструктор")]' #кнопка "Конструктор"
    LOGO_STELLAR_BURGERS = By.XPATH, '//*[contains(@fill, "none")]' #логотип stellar burgers
    EXIT_BUTTON = By.XPATH, '//*[contains(text(), "Выход")]' #кнопка "Выход" в личном кабинете
    ROLLS = By.XPATH, '//*[contains (@class, "text_type_main-default") and contains(text(), "Булки")]' #вкладка "Булки" на странице конструктора
    SAUCES = By.XPATH, '//*[contains (@class, "text_type_main-default") and contains(text(), "Соусы")]' #вкладка "Соусы" на странице конструктора
    FILLINGS = By.XPATH, '//*[contains (@class, "text_type_main-default") and contains(text(), "Начинки")]' #вкладка "Начинки" на странице конструктора
    SAUCE_TRADITIONAL_GALACTIC = By.XPATH, '//*[contains(text(), "Соус традиционный галактический")]' #соус традиционный галактический на вкладке соусов
    MARTIAN_MAGNOLIA_BIO_CUTLET = By.XPATH, '//*[contains(text(), "Биокотлета из марсианской Магнолии")]' # биокотлета из марсианской Магнолии на вкладке начинок
    FLUORESCENT_BUN = By.XPATH, '//*[contains(text(), "Флюоресцентная булка R2-D3" )]' #флюоресцентная булка R2-D3 на вкладки булок







