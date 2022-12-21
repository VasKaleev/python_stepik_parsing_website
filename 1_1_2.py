
# coding: UTF-8


""" print("Парсим сайт")
import requests
response = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html') # get-запрос
s=response.text.encode("utf-8") 
s=str(s)
print(response.encoding)
print("C++",s.count("C++"))
print("Python",s.count("Python")) """

#from urllib.request import urlopen
#html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
#s = str(html)
#print(s.count("Python"), s.count("C++"))
#print(s.encode("utf-8"))
#print(b'html'.decode('utf-8'))
#print(u'\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85'.encode("utf-8"))
print("Парсим сайт")
from re import UNICODE
from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode()
print(html.encode())

    