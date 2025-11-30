import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Firefox()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(10)
    current_url = driver.current_url
    "Ex: https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # if "Admin" in current_url:
    #     print("We are in Dashboard")
    # else:
    #     print("We are not in dashboard")

    assert "Dashboard" in current_url, "Admin not in the URL"

    heading = driver.find_element(By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module").text

    if "Dashboard" == heading:
        print("We are in Dashboard")
    else:
        print("We are not in dashboard")
        raise Exception("We are not in dashboard")


def test_login_with_invalid_cred():
    driver = webdriver.Firefox()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Sivanesh")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("Sivanesh123")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,
                        "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
    time.sleep(10)

    assert True != driver.find_element(By.XPATH, "//p[text()='Invalid credentials']").is_displayed(), "Didn't get the Error message"


def test_extract_test():
    driver = webdriver.Firefox()
    driver.get("https://facebook.com")
    text =driver.find_element(By.TAG_NAME, "html").text
    print(text)






