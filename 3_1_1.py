import xmltodict

with open('map.osm', 'r', encoding='cp1251') as fd:
    doc = xmltodict.parse(fd.read())
print(doc)