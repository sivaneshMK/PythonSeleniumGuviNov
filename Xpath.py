import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("product_name", [
    ("Apple iPhone 17 Pro (Deep Blue, 256 GB)"),  # Test case 1
    ("Apple iPhone 17 Pro Max (Cosmic Orange, 256 GB)"),  # Test case 2
    ("Apple iPhone 17 Pro Max (Silver, 256 GB)")  # Test case 3
])
def test_product_list(product_name):
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    print(driver.title)
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys("iphone")
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[contains(text(),'17')]/span[contains(text(),'iphone')])[1]").click()
    time.sleep(5)
    price = driver.find_element(By.XPATH, "//div[text()='"+product_name+"']/parent::div/following-sibling::div/div[1]").text
    print(price)

def test_product_price():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@name='q']").send_keys("iphone")
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[contains(text(),'17')]/span[contains(text(),'iphone')])[1]").click()
    time.sleep(5)

    product_name = driver.find_elements(By.XPATH, "//a[@class='k7wcnx']//div[@class='RG5Slk']")

    product_price = driver.find_elements(By.XPATH, "//a[@class='k7wcnx']//div[@class='col col-5-12 mao5dl']/div[1]")

    product_details = {}
    for i in range(len(product_name)):
        product_details[product_name[i].text]= product_price[i].text

    print(product_details)

    '''
    {'Apple iPhone 17 (Sage, 256 GB)': '₹82,900',
     'Apple iPhone 17 Pro Max (Silver, 256 GB)': '₹1,49,900', 
     'Apple iPhone 17 Pro (Deep Blue, 256 GB)': '₹1,34,900', 
     'Apple iPhone 17 Pro Max (Deep Blue, 512 GB)': '₹1,69,900', 
     'Apple iPhone 17 Pro (Cosmic Orange, 256 GB)': '₹1,34,900',
    'Apple iPhone 17 Pro Max (Silver, 512 GB)': '₹1,69,900',
    'Apple iPhone 17 Pro Max (Cosmic Orange, 256 GB)': '₹1,49,900', 
    'Apple iPhone 17 Pro (Cosmic Orange, 512 GB)': '₹1,54,900',
    'Apple iPhone 17 Pro (Silver, 512 GB)': '₹1,54,900', 
    'Apple iPhone 17 Pro Max (Deep Blue, 256 GB)': '₹1,49,900',
    'Apple iPhone 17 Pro Max (Deep Blue, 1 TB)': '₹1,89,900',
    'Apple iPhone 17 Pro Max (Silver, 2 TB)': '₹2,29,900', 
    'Apple iPhone 17 Pro (Deep Blue, 512 GB)': '₹1,54,900',
    'Apple iPhone 17 Pro Max (Cosmic Orange, 2 TB)': '₹2,29,900',
    'Apple iPhone 17 Pro (Cosmic Orange, 1 TB)': '₹1,74,900',
    'Apple iPhone 17 Pro Max (Deep Blue, 2 TB)': '₹2,29,900',
    'Apple iPhone 17 Pro (Silver, 1 TB)': '₹1,74,900',
    'Apple iPhone 17 Pro (Deep Blue, 1 TB)': '₹1,74,900',
    'Apple iPhone 17 (Black, 256 GB)': '₹82,900',
    'Apple iPhone 17 (Mist Blue, 256 GB)': '₹82,900',
    'Apple iPhone 17 (Lavender, 256 GB)': '₹82,900',
    'Apple iPhone 17 (White, 256 GB)': '₹82,900',
    'Apple iPhone 17 (Black, 512 GB)': '₹1,02,900',
    'Apple iPhone 17 (Mist Blue, 512 GB)': '₹1,02,900'}

============================================================
    
    '''

def test_table():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.booking.com/index.en-gb.html")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@data-testid='searchbox-dates-container']").click()
    time.sleep(5)
    date = driver.find_element(By.XPATH,
                        "//h3[contains(text(),'December 2025')]/following-sibling::table/tbody//td//span[text()='5']")

    #driver.execute_script("arguments[0].scrollIntoView(true);", date)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
    time.sleep(5)
    date.click()
    time.sleep(10)

def test_demo():
    driver = webdriver.Firefox()
    driver.get("https://admin-demo.nopcommerce.com/")
    time.sleep(10)