import time

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_language(start_browser):

    driver = start_browser
    driver.find_element(By.XPATH, "//a[@title='Show more languages']").click()
    time.sleep(5)
    languages = driver.find_elements(By.XPATH, "//div[@id='language_container']//a")

    lang_list = []
    for elements in languages:
        lang_list.append(elements.text)

    print(lang_list)
    #
    # for langs in lang_list:
    #     driver.find_element(By.XPATH, "(//div[@id='language_container']//a[text()='" + langs + "'])[1]").click()
    #     expec_chk = driver.find_element(By.XPATH, "(//div[@id='pageFooter']//ul/li)[1]").text
    #     assert langs == expec_chk, "Selected language is not matched!!"

    time.sleep(6)


def test_getAttribute():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.XPATH, "//a[@title='Show more languages']").click()
    xpath_getlangs = wait.until(EC.visibility_of_all_elements_located(
        (By.XPATH, "//div[@class='intl-region-none selected-intl-region1']//a")))

    listelement_text = {}

    for element in xpath_getlangs:
        langtext = element.text
        langattribute = element.get_attribute("lang")
        listelement_text[langattribute] = langtext
    driver.quit()

    print(listelement_text)
    return tuple(listelement_text.items())


@pytest.mark.parametrize("langcode,expected_lang", test_getAttribute())
def test_language(langcode, expected_lang):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")

    wait = WebDriverWait(driver, 10)

    driver.find_element(By.XPATH, "//a[@title='Show more languages']").click()
    langcode_xpath = f"//div[@id='language_container']//div[@class='intl-region-none selected-intl-region1']//a[@lang='{langcode}']"
    wait.until(EC.visibility_of_element_located((By.XPATH, langcode_xpath))).click()
    text_to_be_validated = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//ul[contains(@class,'localeSelectorList')]/li[1]"))).text
    print('test', text_to_be_validated)
    assert text_to_be_validated == expected_lang, "Incorrect link"
    driver.quit()



