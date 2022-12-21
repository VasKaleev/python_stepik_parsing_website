
import re
from urllib.request import urlopen        
from bs4 import BeautifulSoup
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
html = resp.read().decode('utf8').split()
a=[int(i) for i in html if i.isdigit()]
print(sum(a))