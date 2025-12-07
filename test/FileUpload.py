from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_upload_file():
    option =Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(option)
    driver.get("https://formy-project.herokuapp.com/fileupload")
    driver.find_element(By.XPATH, "//input[@id='file-upload-field']").send_keys("C:\\Users\\sivan\\Downloads\\Gowtham Internship Letter.pdf")
