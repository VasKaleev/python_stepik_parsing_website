from urllib.request import urlopen
import re
s = ''
html = urlopen("D:\Python\Parsing_website\1.html").read().decode("utf-8")
#html = urlopen("http://svitanok.01sh.ru/").read().decode("utf-8")
s = str(html)
d = dict()
print(s.count("<code>"))
print(s.count('</code>'))
ar = re.findall(r'<code>([a-z]{2,})</code>', s)
#ar=re.findall(r'<code>(.*?)</code>', s)
print(len(ar))
print(ar)
d = dict()
for a in ar:
    try:   d[a] += 1
    except KeyError: d[a] = 1
print(d)
print(sorted(d.items(), key=lambda item: item[1],reverse=True))