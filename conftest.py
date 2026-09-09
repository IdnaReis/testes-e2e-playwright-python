import pytest

@pytest.fixture(autouse=True)
def set_default_timeout(page):
    page.set_default_timeout(60000)
