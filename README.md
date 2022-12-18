# Sprint_3
Реализованные тесты:
Файл locators.py - в нем собраны локаторы, которые использовались в тестах

Файл test_registration.py:
Метод test_registration_correct_values_registration_success(): проверяем успешную регистрацию с корректно введенными значениями. Переход на страницу регистрации осуществляем после кнопки 
"Войти в аккаунт"
Метод test_registration_incorrect_values_registration_failed(): проверяем появление ошибки при вводе некорректного пароля (меньше 6 символов)

Файл test_log_in.py:
Метод test_log_in_from_main_page_button_success(): проверяем вход в аккаунт после кнопки "Войти в аккаунт" и заполнении полей с данными с последующим нажатием "Войти"
Метод test_log_in_through_personal_area_button_success(): проверяем вход в аккаунт после нажатии кнопки "личный кабинет", заполнения данных и нажатия кнопки "Войти"
Метод test_log_in_from_registration_form_success(): проверяем вход в аккаунт из поля для регистрации нажатием кнопки "войти" (страница с данными для регистрации), заполнением полей и нажатием кнопки "Войти"
(страница с воодом данных для входа в аккаунт)
test_log_in_from_password_recovery_form_success(): проверяем вход в аккаунт из страницы для восстановления пароля нажатием кнопки "войти" (страница с восстановлением пароля), заполнением полей и 
нажатием кнопки "Войти (страница с воодом данных для входа в аккаунт)"

Файл test_personal_area_enter.py:
Метод test_personal_area_enter_after_click_button_success(): проверяем переход в личный кабинет с главной страницы после того, как залогинились в аккаунт

Файл test_jump_to_constructor.py:
Метод test_jump_to_constructor_from_personal_area_success(): проверяем переход на страницу конструктора из личного кабинета нажатием на кнопку "Конструктор"

Файл test_jump_to_main_page_by_logo.py:
Метод test_jump_to_main_page_by_logo_success(): проверяем переход на главную страницу из личного кабинета по нажатию на логотип stellar burgers

Файл test_exit_button.py:
Метод test_exit_button_from_personal_area_success(): проверяем выход из аккаунта из личного кабинета нажатием кнопки "Выход"

Файл test_switching_between_sections.py:
Метод test_switching_to_sauces_from_rolls_success(): проверяем переключение на вкладку "Соусы" из вкладки "Булки"
Метод test_switching_to_fillings_from_rolls_success(): проверяем переключение на вкладку "Начинки" из вкладки "Булки"
Метод test_switching_to_rolls_from_sauces_success(): проверяем переключение на вкладку "Булки" из вкладки "Соусы"