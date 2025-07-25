import pytest

from selene import browser

@pytest.fixture
def teardown():
    yield
    print("do something")

#Открыть браузер
@pytest.fixture()
def open_browser():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True

#Авторизоваться
@pytest.fixture()
def authorization():
    # Открыть в браузере сайт "Степик"
    browser.open('https://stepik.org/')
    #browser.config.timeout = 8.0
    # Кликнуть кнопку "Войти"
    browser.element('a[id=ember467]').click()
    # Указать Email и Password
    browser.element('input[id=id_login_email]').type('vasya1601@mail.ru')
    browser.element('input[id=id_login_password]').type('123-qwe')
    # Кликнуть кнопку "Войти"
    browser.element('.sign-form__btn').click()


#vasya1601@mail.ru
#123-qwe
