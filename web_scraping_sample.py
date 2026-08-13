import requests
from bs4 import BeautifulSoup
import re
url = "https://blog.python.org/blog/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html5lib")
tag1 =soup.find("h1")
print(tag1(strip=True))
tag = soup.find_all("h3")
for title in  tag:
  print(title.get_text (strip=True))
authors = soup.find_all("a", href=re.compile(r"^/authors/"))

for author in authors:
    print(author.get_text(strip=True))
