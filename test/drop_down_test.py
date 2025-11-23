import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_drop_down(start_browser):
    driver = start_browser
    driver.find_element(By.XPATH, "//a[text()='Create new account']").click()
    time.sleep(3)
    day = driver.find_element(By.XPATH, "//select[@aria-label='Day']")
    s1 = Select(day)
    s1.select_by_index(2)

    month = driver.find_element(By.XPATH, "//select[@title='Month']")
    s2  = Select(month)
    s2.select_by_value("12")

    year = driver.find_element(By.XPATH, "//select[@name='birthday_year']")
    s3 = Select(year)
    s3.select_by_visible_text("1995")
    years = s3.options
    for ye in years:
        print(ye.text)

    # count number of option
    print(len(years))

    #last option in the list box
    print(years[len(years)-1].text)

    #print selected option
    print(s3.first_selected_option.text)
