import xmltodict
from pprint import pprint    
xml = ('''

    <mydocument has="an attribute">
        <and>
            <many>elements</many>
            <many>more elements</many>
        </and>
        <plus a="complex" b="hello">
            element as well
        </plus>
    </mydocument>


    ''')
#pprint(xmltodict.parse(xml))
print(xmltodict.parse(xml))