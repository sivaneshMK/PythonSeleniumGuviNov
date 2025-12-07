import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_alert():
    driver=  webdriver.Chrome()
    driver.get("https://demoqa.com/alerts")
    click_me= driver.find_element(By.XPATH, "//button[@id='confirmButton']")
    driver.execute_script("arguments[0].scrollIntoView();", click_me)
    click_me.click()
    #alert =driver.switch_to.alert
    wait = WebDriverWait(driver, 10)
    alert = wait.until(expected_conditions.alert_is_present())
    message = alert.text
    print(message)
    #alert.accept()
    alert.dismiss()
    time.sleep(30)

def test_prompt_alert():
    driver=  webdriver.Chrome()
    driver.get("https://demoqa.com/alerts")
    click_me= driver.find_element(By.XPATH, "//button[@id='promtButton']")
    driver.execute_script("arguments[0].scrollIntoView();", click_me)
    click_me.click()
    #alert =driver.switch_to.alert
    wait = WebDriverWait(driver, 10)
    alert = wait.until(expected_conditions.alert_is_present())
    alert.send_keys("Guvi")
    time.sleep(5)
    alert.accept()
    driver.save_screenshot("C:\\Users\\sivan\\PycharmProjects\\PythonSeleniumGuviNov\\test\\Screenshots\\alert.png")

    time.sleep(10)
