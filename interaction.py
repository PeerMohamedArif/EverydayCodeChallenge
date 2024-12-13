from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)
# driver= webdriver.Chrome()
#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# time.sleep(random.randint(5,10))
# stats=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# # print(stats.text)
# #stats.click()
#
# all_portals=driver.find_element(By.LINK_TEXT,value="Content portals")# finds based on the text in the front end
# # all_portals.click()
# # time.sleep(random.randint(5,10))
#
# # how to type?
# search=driver.find_element(By.NAME,value="search")
# search.send_keys("Python",Keys.ENTER)
# # search.send_keys(Keys.ENTER)


chrome1_options=webdriver.ChromeOptions()
chrome1_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome1_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
FN=driver.find_element(By.NAME,"fName")
FN.click()
FN.send_keys("Arif",Keys.TAB)
LN=driver.find_element(By.NAME,"lName")
LN.send_keys("Mohamed",Keys.TAB)
Email=driver.find_element(By.NAME,"email")
Email.send_keys("arif@gmail.com",Keys.ENTER)
submit=driver.find_element(By.CLASS_NAME,"btn")
submit.send_keys(Keys.ENTER)
time.sleep(random.randint(30,60))
driver.quit()
