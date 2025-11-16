import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# start browser
driver = webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT, "Admin").click()
# driver.get("https://facebook.com")
# driver.find_element(By.XPATH, "//div[@class='_6lux']//input").send_keys("abcd")
# driver.find_element(By.XPATH,"//div[@class='_6lux']//input").send_keys("1233")
