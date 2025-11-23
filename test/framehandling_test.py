'''
iframe --> inline frame

Where --> it is mostly used to load Ad

why --> ad will be loaded from different source

ad are differce in size(pixel) and type

iframe will be create inside the HTML
tag will be <iframe>
    <HTML>
        <head>
        </head>

        <body>
            <input type="text"></input>
            <iframe>
                <input type="text"></input>

            </iframe>

        </body>

    </HTML>

... </iframe>


'''
import time

from selenium.webdriver.common.by import By


def test_iframe(launch_thandhi):
    driver=launch_thandhi
    time.sleep(50)
    frame1 = driver.find_element(By.XPATH, "//div[@id='home_top_right_level_1']//iframe")
    driver.switch_to.frame(frame1)
    #by using name or id attribute value
    #driver.switch_to.frame("google_ads_iframe_/313420551/dt_home_r1_300x250_0")
    driver.find_element(By.TAG_NAME, "a").click()
    '''
    handling iframe by using 
    1. webelement
    2. name
    3. id

    '''

