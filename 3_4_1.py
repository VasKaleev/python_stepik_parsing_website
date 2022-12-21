

import xmltodict
import urllib.request
urllib.request.urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=29.9911%2C53.0915%2C30.1259%2C53.1172','map.osm')
fin = open('map.osm', 'r', encoding='utf8')
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
                if '@k' in tag and tag['@k']=='shop' and tag['@v']=='supermarket':
                    shops+=1
                    flag=True
                if '@k' in tag and tag['@k']=='name':
                    name=tag['@v']
        if flag:
            names.append(name)
print(shops)
print(*names)
