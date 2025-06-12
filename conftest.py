import pytest


@pytest.fixture
def teardown():
    yield
    print("do something")