

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
                if '@k' in tag and tag['@k']=='shop' and tag['@v']=='supermarket':
                    shops+=1
                    flag=True
                if '@k' in tag and tag['@k']=='name':
                    name=tag['@v']
        if flag:
            names.append(name)
print(shops)
print(*names)
