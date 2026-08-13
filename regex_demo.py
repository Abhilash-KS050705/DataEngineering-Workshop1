import requests
from bs4 import BeautifulSoup

url = "YOUR_URL"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html5lib")

tag = soup.find("h3")

print(tag)
