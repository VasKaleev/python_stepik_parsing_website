# coding: utf8
"""
from urllib.request import urlopen
import re
#Парсинг сайта через библиотеку urlopen
s = ''
html = urlopen("https://mineplex.io/ru").read().decode("utf-8")
#html = urlopen("http://svitanok.01sh.ru/").read().decode("utf-8")
s = str(html)
#print(html)
pos = s.find('<a href=')
while pos != -1:
    posguate = s.find('"', pos+9)
    href = s[pos+9:posguate]
    print(href)
    pos = s.find('<a href=',pos+1)

#Определяем количечтво гиперссылок <a hreh=> на сайте    
print("Количество гиперссылок на сайте <a href=",s.count("<a href="))
print(s.count('</a>'))
print(s.title) 
"""
#############################################################
#Парсинг сайта через библиотеку requests
#Определяем количечтво гиперссылок < hreh=> на сайте
# через задание шаблона поиска с помощью регулярных выражений 
import requests
import re
#response = requests.get('https://mineplex.io/ru')  # get-запрос
response = requests.get('https://mineplex.io/ru')
webpage = response.text
response.encoding="utf-8"
s = str(webpage)
#print(s) 
#regex = ('<a>(.*?)</a>')
regex = ('href="https://(.*?)"')
l = re.findall(regex, webpage)
count=0
print("Гиперссылки сайта https://mineplex.io/ru")
print("Поиск по тексту href='https://'")
for i in l:
    count+=1
    print(count,")",i) 

""" #############################################################
#Парсинг сайта через библиотеку requests
from urllib.request import Request
import requests
response = requests.get('https://mineplex.io/ru')  # get-запрос
s = response.text
s = str(s)
print(response)
#print(response.headers)
#print(response.json)
print(response.status_code)
print(response.cookies)
#print(response.content)
print(response.url)     """