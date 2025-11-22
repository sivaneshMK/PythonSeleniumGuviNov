import time

import pytest
from selenium.webdriver.common.by import By


def test_window_handling(start_ohrms):
    driver = start_ohrms
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@class='oxd-glass-button orangehrm-upgrade-button']").click()
    time.sleep(10)
    # get the current window reference
    parent_window = driver.current_window_handle

    all_windows = driver.window_handles
    # window_handles
    '''
    is a webdriver method, is used to get all the windows which is opened
    and it will return the windows references in list format
    
    '''
    print(all_windows)
    print(len(all_windows))
    driver.switch_to.window(all_windows[1])

    '''
    switch_to.window()
    method used to switch to the particular window based on window ref
    
    '''

    driver.find_element(By.XPATH, "//input[@name='FullName']").send_keys("Sivanesh")
    # close method will close the current window
    #driver.close()

    time.sleep(15)
    # quite method will close the entire browser
    #driver.quit()

    #switch back to the parent window
    driver.switch_to.window(parent_window)

    driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[text()='Logout']").click()

    # get the current window reference
    #current_window = driver.current_window_handle

    '''
    XPATH:
    ------
    2 type of xpath
    ----------------
    absolute xpath
    ----------------
        it is start from /html/body/......current tag
        root node... current node
    
    
    relative xpath
    -------------------
    Xpath --> XML Path
    
    //tagname[@propertyname = 'property value']
    //tagname[text()='text of the element']
    //tagname[contains(@propertyname, 'property value')]
    //tagname[contains(text(), 'text of the element')]
    
    Advantage in xpath
    -------------------
    we can traverse back and forth in the html dom structure
    we can find the element using text too
    we can identify the element by using the element relation ship
 
    '''

