#############################################################
#Парсинг сайта через библиотеку requests
#Определяем количечтво гиперссылок 
#через задание шаблона поиска с помощью регулярных выражений 
import requests
import re
#response = requests.get('https://dev.mineplex.finance/ru')  # get-запрос
response = requests.get('https://mineplex.io/ru')
webpage = response.text
response.encoding="utf-8"
s = str(webpage)
#print(s) 
#regex = ('<a>(.*?)</a>')
regex = ('href="https://(.*?)"')
l = re.findall(regex, webpage)
count=0
print("Cайт https://mineplex.io/ru")
print("Поиск по тексту href=\"https://")
a=[]
with open('parsing.txt','a',encoding='utf-8') as file:
    for i in l:
        count+=1
        b=str(count)+")"+i
        a.append(b)
        print(b)
        file.writelines(b+"\n")        


regex = ('src="https://(.*?)"')
l = re.findall(regex, webpage)
count=0
print("Cайт https://mineplex.io/ru")
print("Поиск по тексту src=\"https://")
with open('parsing.txt','a',encoding='utf-8') as file:
    for i in l:
        count+=1
        b=str(count)+")"+i
        a.append(b)
        print(b)
        file.writelines(b+"\n")       

