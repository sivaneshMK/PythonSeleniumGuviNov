from selenium.webdriver.common.by import By


def test_signup(start_browser):
    driver = start_browser
    driver.find_element(By.LINK_TEXT, "Create a Page").click()


