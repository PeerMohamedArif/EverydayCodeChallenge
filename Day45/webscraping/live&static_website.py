from bs4 import BeautifulSoup
import requests

#live
#response=requests.get("https://news.ycombinator.com/")
#response.raise_for_status()
#static
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage=response.text

yc_soup=BeautifulSoup(yc_webpage,"html.parser")
#getting the headline for the first post
article_tags=yc_soup.select(selector=".titleline a")
article_texts=[]
article_links=[]

for article_tag in article_tags:
    article_text=article_tag.getText()
    article_texts.append(article_text)

    article_link=article_tag.get("href")
    article_links.append(article_link)

article_upvotes =[int(score.getText().split()[0]) for score in yc_soup.findAll(name="span", class_="score")]

largest_upvotes=max(article_upvotes)
index_of_largest_upvotes=article_upvotes.index(largest_upvotes)

print(f"Article: \"{article_texts[index_of_largest_upvotes ] }\" with the link:{article_links[index_of_largest_upvotes]} has the highest upvotes of {largest_upvotes} points at this moment.")

