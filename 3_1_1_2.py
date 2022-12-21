import xmltodict
print(dict(xmltodict.parse("""<?xml version='1.0' ?>
  <person>
  <name>Jon</name>
  </person>""")))
#print({u'person':{u'name'}})