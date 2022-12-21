
import xmltodict
fin = open('map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
shops=0
names=[]
dct = xmltodict.parse(xml)
for node in dct['osm']['node']:
    if 'tag' in node:
        tags=node['tag']
        flag=False
        name='noname'
        if isinstance(tags,list):
            for tag in tags:
                if '@k' in tag and tag['@k'] == "amenity" and tag['@v']=='fuel':
                    shops += 1
        elif isinstance(tags, dict):
            if (tags['@v']) == 'fuel':
                    shops +=1
print(shops)
print(*names)
"""
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'lxml').find_all('node')
s = BeautifulSoup(str(soup), 'lxml').find_all('tag', k='amenity', v='fuel')
print(len(s))
"""