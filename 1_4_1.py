import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p', class_='outer-text')
print(soup) 

""" import re
from urllib.request import urlopen
html = str(urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8'))
regular = re.findall(r'<a.*?href="([^"]*?)"', html)
print(*regular, sep='\n') """

""" from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# href = soup.find_all('a')
# print(*[c["href"] for c in href if c.get("href") is not None], sep='\n')
# Или так как в видео
href = soup.find_all('a', href=True)
print(*[c["href"] for c in href], sep='\n') """

