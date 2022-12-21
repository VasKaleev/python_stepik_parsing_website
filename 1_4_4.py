import re
from urllib.request import urlopen        
from bs4 import BeautifulSoup
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
for i in soup:
    a=re.findall(' (\d*) ', str(i))
print(sum([int(i) for i in a]))


""" from urllib.request import urlopen
html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8').split()
res = []
#print(html)
for i in html:
    if i.isdigit():
        res.append(int(i))
print(sum(res)) """

""" from urllib.request import urlopen
html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8').split()
res = []
#print(html)
a=[int(i) for i in html if i.isdigit()]
print(sum(a)) """