import xmltodict
fin=open('map2.osm', 'r', encoding='utf-8')
text = fin.read()
fin.close()
count=0
count1=0
dct=xmltodict.parse(text)
#print(parse['osm']['node'][100])
for node in dct['osm']['node']:
    if 'tag' in node:
        count+=1
    elif 'tag' not in node:
        count1+=1
print(count)
print(count1)


"""     
        tags=node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@k']=='shop':
                    shops+=1
print(shops)
                #print(tag)
            #print()
        #if '@k' in tag:
        #    print(tag['@k'])
"""