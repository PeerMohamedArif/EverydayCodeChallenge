from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options=chrome_options)
cookie_clicker_url="https://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_clicker_url)

def check_store():
    store_items=driver.find_elements(By.CSS_SELECTOR, "#store div")
    money=int(driver.find_element(By.ID,"money").text.replace(",","").strip())
    chosen_item=store_items[0]
    for store_item in store_items:
        try:
            store_item_price= int(store_item.text.split("-")[1].split("\n")[0].strip().replace(",",""))
            if store_item_price<=money:
                chosen_item=store_item
        except IndexError:
            continue
    chosen_item.click()

interval=time.time() +10 # waits for 10 seconds
end_clicker=time.time() + (60*5) # 5 minutes

cookie=driver.find_element(By.ID,"cookie")
while True:
    cookie.click()

    if time.time()>= interval:
        interval+=10
        check_store()

    if time.time()>=end_clicker:
        break
driver.quit()