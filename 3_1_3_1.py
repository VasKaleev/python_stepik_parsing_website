import xmltodict
fin=open('map.osm', 'r', encoding='utf-8')
xml = fin.read()
fin.close()
parse=xmltodict.parse(xml)
print(parse['osm']['node'][100])