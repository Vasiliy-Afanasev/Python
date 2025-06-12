import random

import pytest


@pytest.fixture(scope="session")
def browser():
    print("Открываем браузер")
    yield random.randint(0, 100)
    print("Закрываем браузер")


@pytest.fixture
def get_admin(browser, teardown):
    return random.randint(0, 100)


def test_simple(get_admin, browser):
    # assert  get_admin == 5, "ID администратора ожидался 5"
    # assert browser == "Chrome"
    print(browser)
    assert 1 == 1, "Единица не должны быть равна двойке"


def test_another(browser,  get_admin):
    print(browser)
    # assert get_admin == 5, "ID администратора ожидался 5"
    assert 1 == 1, "Единица не должны быть равна двойке"
