from bs4 import BeautifulSoup
import requests
import smtplib as smtp
import os
from dotenv import load_dotenv

load_dotenv()

my_email=os.environ["EMAIL_ADDRESS"]
my_password=os.environ["EMAIL_PASSWORD"]
BUY_PRICE=30
#remember select returns a list whereas find returns the value so you cant get a text from a list.
# select accepts css selectors whereas find does not

practice_url = "https://appbrewery.github.io/instant_pot/"
url = ("https://www.amazon.com/Adapter-MacBook-2018-2023-Gigabit-Ethernet/dp/B0D78LSVHH/ref=sr_1_3?crid=241K6EH6J14TI&dib=eyJ2IjoiMSJ9.s-Q4Vjme-rN55fU94bj5ql1LFKCRWV7p1extuk0gVUk5BiBTnaJtHGjMCximDDFJR0q2aY5RT1CFMtEdnxxLwgWYCwPvfkrZiCt0zOwGB36YLThvQgLhULbsxTVB2-Aut2l8N-1XTsXhcWZBx2aG9WYfVgNuxnYCbunS9XobM4KteOEHNfQ1f3cm_pzRd60Qj9KIAvWFxzJiNrWRzJ7bWGMCStE7mCjb6MN2vOCHvPc.EDBTLWmcToobRbZ9IppLnys6NSnVePb0ZmG1UttADVo&dib_tag=se&keywords=pepper+jobs&qid=1733809386&sprefix=pepper+jobs%2Caps%2C457&sr=8-3")

response=requests.get(url=url,headers={ "Accept-Language": "en-US,en;q=0.9,ta;q=0.8",
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                                              "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"})
amazon_text=response.content

soup=BeautifulSoup(amazon_text,"html.parser")
price=soup.find("span",class_="a-offscreen").get_text()
price_without_currency=price.split("$")[1]
price_float=float(price_without_currency)
title=soup.find(id="productTitle").get_text().strip()

if price_float< BUY_PRICE:
    message=f"{title} is on sale for {price}"
    with smtp.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result=connection.login(my_email,my_password)
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Amazon Price Alert!!\n\n{message}\n{url}".encode("utf-8")
                            )
        connection.close()

