import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_web_element_method():
    option = Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(option)
    driver.get("https://www.facebook.com/")
    driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()='Create a new account']")))
    female_radio_btn = driver.find_element(By.XPATH,"//label[text()='Female']/input")
    if female_radio_btn.is_selected():
        print("Female radio button is already selected")
    else:
        female_radio_btn.click()
        print("Female radio button is selected")


def test_clear_method():
    option = Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(option)
    driver.get("https://admin-demo.nopcommerce.com/login")

    username = driver.find_element(By.XPATH, "//input[@name='Email']")
    username.clear()
    username.send_keys("abcd@gmail.com")


def test_api():

    response = requests.post(url="https://reqres.in/api/login", json='''{"username": "sivanesh","email": "sivaneshmk4@gmail.com", "password": "Sivanesh@2123"}''')

    print(response.status_code)
    assert response.status_code == 200,  "The Status code is not matched"
    print(response.content)


'''
Rest --> 
soap --> XML
Resassured 
'''