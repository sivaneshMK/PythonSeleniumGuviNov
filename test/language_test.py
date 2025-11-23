from selenium import webdriver
from selenium.webdriver.common.by import By


def test_language():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.find_element(By.LINK_TEXT, "தமிழ்").click()
    actual_title = driver.title
    assert actual_title == "Facebook - உள்நுழையவும் அல்லது பதிவுசெய்யவும்", "The Title is Not Expected"
    actual_url = driver.current_url
    assert actual_url == "https://facebook.com/", "URL is not as expected"
    actual_static_message = driver.find_element(By.CLASS_NAME, "_8eso").text
    assert actual_static_message == "Facebook சக மனிதர்களுடன் நல்லுறவு அமைத்துக்கொள்ள உதவுகிறது.", ("The Static message is not Expected")
