import pytest
from selenium import webdriver


@pytest.fixture
def start_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    return driver

@pytest.fixture
def start_ohrms():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    return driver