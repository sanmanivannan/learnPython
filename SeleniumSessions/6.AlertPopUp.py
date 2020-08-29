from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

#Code to overcome JAVASCRIPT POPUP ALERT
"""driver.get('https://businessemail.rediff.com/manageserviceslogin')
driver.implicitly_wait(5)
print(driver.title)
sub_button = driver.find_element(By.CLASS_NAME, 'button')
sub_button.click()

alartmsg = driver.switch_to.alert
print(alartmsg.text)
alartmsg.accept()
#alartmsg.dismiss()
#alartmsg.send_keys()
driver.switch_to.default_content()
driver.quit()"""

#Code to overcome FRAMEs
"""driver.get('https://businessemail.rediff.com/manageserviceslogin')
driver.implicitly_wait(5)
print(driver.title)
#driver.switch_to.frame(2)#providing the INDEX number of the frame
#driver.switch_to.frame('nameoftheframe') # providing the name of the frame
headervalue = driver.find_element(By.CSS_SELECTOR, 'body >he').text
print(headervalue)
#driver.switch_to.parent_frame()
"""

#Handling Authentication POPUP
"""driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth') #providing the credentials on the URL itself"""

#Handling File Uploads

driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.find_element(By.NAME, "upfile").send_keys("C:\\Users\\Vishnuram\\Desktop\\test.txt")
driver.find_element(By.XPATH, "/html/body/form/input[3]").click()






