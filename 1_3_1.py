from urllib.request import urlopen
from bs4 import BeautifulSoup
s = ''
#html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode("utf-8")
html = urlopen("http://svitanok.01sh.ru/").read().decode("utf-8")
s = str(html)
pos = s.find('<a href=')
while pos != -1:
    posguate = s.find('"', pos+9)
    href = s[pos+9:posguate]
    print(href)
    pos = s.find('<a href=',pos+1)