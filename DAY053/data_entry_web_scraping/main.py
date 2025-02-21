from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

GOOGLE_FORMS_LINK= (" # *********your google doc link ********** #")
ZILLOW_LINK="https://appbrewery.github.io/Zillow-Clone/"
# Beautiful Soup
web_response=requests.get(url=ZILLOW_LINK)
content_webpage=web_response.text
soup=BeautifulSoup(content_webpage,"html.parser")
all_cards_address=soup.find_all(name="address")
all_cards_links= soup.find_all(name="a",class_="property-card-link")
all_card_price=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
all_card_links = [tag.get("href") for tag in all_cards_links]
all_address_list = [address.get_text(strip=True) for address in all_cards_address]
all_price_list=[price.get_text(strip=True) for price in all_card_price]
merged_list = [[x, y, z] for x, y, z in zip(all_address_list, all_price_list, all_card_links)]
# Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_FORMS_LINK)
for each_card in merged_list:
    address_entry = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]"
                                                  "/div/div[1]/div/div[1]/input")
    price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                '/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                               'div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.CLASS_NAME, "QvWxOd")
    address_entry.click()
    address_entry.send_keys(each_card[0],Keys.TAB)
    # time.sleep(3)
    price_entry.send_keys(each_card[1],Keys.TAB)
    # time.sleep(3)
    link_entry.send_keys(each_card[2],Keys.TAB)
    # time.sleep(3)
    submit.click()
    # time.sleep(1)
    next_form = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_form.click()
    # time.sleep(2)
# time.sleep(15)
driver.quit()
