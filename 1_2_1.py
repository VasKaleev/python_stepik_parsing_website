from urllib.request import urlopen
s = ''
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode("utf-8")
s = str(html)
print(html)
a = ''
b = []
print(s.count("C++") + s.count('c++'))
#for i in s:
#    a = s[s.find('<'):s.find('>')+1]
#    print(a)
    #b.append(s[s.find('<'):s.find('>')+1])
#    s = s.replace(a, '')
    #b.append(a)
#print(b)

