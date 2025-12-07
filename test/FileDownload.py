import os.path
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_file_download():
    download_path = os.path.join(os.getcwd(), "downloads")
    options = Options()

    prefs = {
        "download.default.directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled":True,
        "profile.default_content_settings.popup": 0,
        "profile.default_content_settings_values.automatic_downloads":1
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.selenium.dev/downloads/")

    link = driver.find_element(By.XPATH, "//p[contains(text(),'Latest stable version')]/a")
    #driver.execute_script("arguments[0].scrollIntoView();", link)
    ac = ActionChains(driver)
    ac.send_keys(Keys.PAGE_DOWN).perform()
    ac.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(5)
    link.click()
    time.sleep(10)
    value = driver.find_element(By.TAG_NAME, "html").text
    print(value)