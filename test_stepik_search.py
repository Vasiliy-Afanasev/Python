import pytest
from selene import browser

#Открыть браузер и авторизоваться
def test_open_browser(open_browser, authorization):
    print("Авторизовались")
#Поиск курса: 'Поколение Python'
    browser.element('.navbar__search-input').type('Поколение Python').press_enter()
    browser.config.timeout = 2.0



