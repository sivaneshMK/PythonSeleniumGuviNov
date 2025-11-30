'''
static wait is not suggestible in real time
static wait --> time.sleep()

implicit wait
-------------
implicit wait is also called global wait
it is applying wait all the elements by default
min wait time is applied for each and ever element is 500ms
max is as user defined

if the element is not in the page selenium will through
no such element exception

when selenium raising the no such element exception
wait statement is comes into picture

it will apply the 500ms wait

poll time

explicit wait
------------------
it is applied for the specific element with specific conditions


fluent wait

'''
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_window_handling(start_browser):
    driver = start_browser
    #driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
    #time.sleep(10)
    number = 1
    for i in range(20):
        time.sleep(0.5)
        print(f"number of poll: {number}")
        number=+1
        try:
            driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys("Guvi")
            break
        except NoSuchElementException as e:
            continue
    else:
        raise NoSuchElementException


def test_window_handling(start_browser):
    driver = start_browser
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
    #time.sleep(10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@aria-label='First name']")))
    element.send_keys("Guvi")




    #driver.find_element(By.XPATH, "//input[@aria-label='First name']").send_keys("Guvi")

def test_fluent_wait(start_browser):
    driver = start_browser
    wait = WebDriverWait(driver, 30, poll_frequency=4, ignored_exceptions=[ElementClickInterceptedException])
    driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
    #time.sleep(10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@aria-label='First name']")))
    element.send_keys("Guvi")

def test_navigation(start_browser):
    driver = start_browser
    driver.find_element(By.LINK_TEXT, "Forgotten password?").click()
    driver.back()
    print(driver.title)
    driver.forward()
    print(driver.title)
    driver.refresh()

def test_drag_and_drop_operations():

    driver = webdriver.Chrome()
    driver.get("https://beej.us/blog/data/drag-n-drop/")
    driver.switch_to.frame(0)
    goat1 = driver.find_element(By.XPATH, "//img[@id='goat2']")
    dropzone1 = driver.find_element(By.XPATH, "//div[text()='This is Dropzone 1']")

    actions = ActionChains(driver)
    #actions.drag_and_drop(goat1, dropzone1).perform()
    actions.click_and_hold(goat1).perform()
    #actions.move_to_element(dropzone1).perform()
    #actions.context_click(goat1).perform()
    actions.double_click(goat1).perform()
    #actions.release().perform()
    driver.switch_to.default_content()
    actions.scroll_to_element(driver.find_element(By.XPATH, "//h2[text()='Drag Details']")).perform()

    time.sleep(10)

def test_Actions_Chains():
    driver = webdriver.Chrome()
    driver.get("http://www.facebook.com")
    username = driver.find_element(By.XPATH, "//input[@id='email']")
    ac = ActionChains(driver)
    ac.click(username).perform()
    ac.send_keys("83989398983839").perform()


