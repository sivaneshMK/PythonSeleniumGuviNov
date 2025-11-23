import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_iframe(launch_thandhi):
    driver=launch_thandhi
    time.sleep(20)
    all_frames = driver.find_elements(By.XPATH, "//iframe[@title='3rd party ad content']")
    for frame in all_frames:
        driver.switch_to.frame(frame)
        try:
            try:
                driver.find_element(By.TAG_NAME, "a").click()
            except ElementNotInteractableException as e:
                # keys enumeration
                driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
            driver.switch_to.default_content()
        except NoSuchElementException as e:
            print("There is link in the frame")
            driver.switch_to.default_content()


'''
launch Thandhi
click each ad
it will open the content in next tab
you can switch to the tab
get title of the tab
and close the tab
'''

