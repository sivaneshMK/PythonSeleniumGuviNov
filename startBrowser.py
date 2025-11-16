import time
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome, firefox, edge, safari
#driver = Chrome()
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
# compound class name can't be used
#driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
time.sleep(5)
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(10)



