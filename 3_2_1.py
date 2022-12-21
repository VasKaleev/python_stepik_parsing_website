import xmltodict
fin=open('map.osm', 'r', encoding='utf-8')
text = fin.read()
fin.close()
dct=xmltodict.parse(text)
#print(parse['osm']['node'][100])
print(dct)