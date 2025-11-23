import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# start browser
driver = webdriver.Chrome()

# get method
'''
get method is a webderiver method 
it is used to launch the application(URL)
'''
driver.get("https://www.facebook.com/")
# dynamic Id Attribute
#driver.find_element(By.ID, "u_0_0_7a").click()

# Find Element method
'''
WebDriver method it is used to locate elements by using the locator value
it will support 8 types of locators()
we have to pass 2 orgument 
1. locator
2. value
if the element is not in the HTML Dom structure it will through an 
Exception NoSuchElementException

if the element is found it will return those elements

return type of findElement method is WebElement Type

findelement method will return first matched element




a = 10




'''
driver.find_element(By.LINK_TEXT, "Create new account").click()

# Send Keys Method
'''
it is a WebElement Method
it is used to enter txt in the text box, pwd txt box, 
multi line text box, search box.

you have pass the data as string argument.


'''

'''
CSS Selector
--------------
tagname[propertyname = 'property value']

tagname#id attribute value

tagname.class Attribute value
(if any space present in the class value u can replace with .(dote))
input.inputtext._58mg._5dba._2ph-


'''

driver.find_element(By.CSS_SELECTOR, "input[aria-label='First name']").send_keys("Sujatha")
driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("A")
login = driver.find_element(By.NAME, "sex")
print(type(login))
driver.find_element(By.NAME, "sex").click()

time.sleep(10)

'''
Click method
--------------
click method is webElement method
it is used to perform action on the webelements like
button, link, radio button, check box ect
'''


