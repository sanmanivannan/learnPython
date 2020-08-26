"""
How to create web element using different locators:
ID
Name
Class Name
XPath
CSS Selector
Link Text
Partial Link Text
Tag Name

"""
from selenium import webdriver  #Importing Selenium Lib
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

#FindElement By ID
driver.find_element(By.ID, "Form_submitForm_FirstName").send_keys("FName")

#FindElement By NAME
driver.find_element(By.NAME, "LastName").send_keys("LName")

#FindElement By CSS SELECTOR, just use the ID or Name value and have #in front of the value
driver.find_element(By.CSS_SELECTOR, "#Form_submitForm_JobTitle").send_keys("Manager")
#FindElement By CLASS_NAME
#driver.find_element(By.CLASS_NAME, "email text").send_keys("test123@gmail.com")

#FindElement By XPATH
driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/ul[2]/li[1]/a').click()
driver.implicitly_wait(5)

#FindElement By LINK_TEXT
driver.find_element(By.LINK_TEXT, "Features").click()


