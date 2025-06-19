import pytest

from selene import browser


def test_open_browser(open_browser):
    print(123)

def test_authorization():
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




