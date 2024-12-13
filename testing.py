from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


#keep chrome browser open after program finishes running
chrome_options=webdriver.ChromeOptions() # modifies a specific option to change the behaviour
chrome_options.add_experimental_option("detach",True) # when detach is true keeps the browser open

driver=webdriver.Chrome(options=chrome_options)



# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# time.sleep(random.randint(10,20))
# price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# price_cents=driver.find_element(By.CLASS_NAME, 'a-price-fraction')
# print(f"The price is {price_dollar.text}.{price_cents.text}")# .text is used to access the content within it



# driver.get("https://www.python.org/")
# search_bar=driver.find_element(By.NAME,"q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# # gives out a selenium element and not the html # to get hold of attribute use .tagname or get_attribute("placeholder") per se
# button= driver.find_element(By.ID,"submit")
# print(button.size) # gets the size



# # Find element by CSS Selector
# documentation_link=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#. is used for class
# <div class="small-widget documentation-widget"> in this case there was two class names
# print(documentation_link.text)

# finding element by XPATH
# driver.get("https://www.python.org/")
# bug_link=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


driver.get("https://www.python.org/")
event_times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
# for time in event_times: # since it is a selenium element we have to iterate
#     print(time.text)
event_names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget .menu a")
# print(event_names[0].text) # the selenium object can be tapped into like a list just for your understanding
# for name in event_names:
#     print(name.text)
events_dictionary={}
for n in range(len(event_times)):
    events_dictionary[n]={
        "time":event_times[n].text,
        "name":event_names[n].text,
    }
print(events_dictionary)


# driver.close() #closes just one tab
driver.quit()# closes entire browser

