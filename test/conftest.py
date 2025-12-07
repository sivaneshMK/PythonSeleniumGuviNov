import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as firefox_options

@pytest.fixture
def start_browser():
    options = Options()
    #options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    return driver

@pytest.fixture
def start_ohrms():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    return driver

@pytest.fixture
def launch_thandhi():
    options = firefox_options()
    #options.add_argument("--headless")
    options.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(options)
    driver.get("https://www.dailythanthi.com/")
    driver.maximize_window()
    return driver

@pytest.fixture()
def launch_chrome():
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_experimental_option("detach", True)
    option.add_argument("--start-maximized")
    option.add_experimental_option("prefs",{"profile.default_content_setting_values.geolocation":2}) # 1-Allow , 2-Block
    driver = webdriver.Chrome(option)
    driver.get("https://www.dailythanthi.com/")
    return driver