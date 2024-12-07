from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
    content=file.read()

soup=BeautifulSoup(content,"html.parser") #instead of html you can use lxml
print(soup.title)
print(soup.title.name)
print(soup.title.string) # title string
print(soup)# entire html file
print(soup.prettify())# indented html
print(soup.a) # first anchor tag
print(soup.li)# first list
print(soup.p)# first paragraph

all_anchor_tags=soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading=soup.find(name="h1",id="name")
print(heading)

section_heading=soup.find(name="h3",class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

# company_url=soup.select(selector="p a") # all matching item
company_url=soup.select_one(selector="p a") # first matching item
print(company_url)

name=soup.select_one(selector="#name") # for id name
print(name)

headings=soup.select(selector=".heading")
