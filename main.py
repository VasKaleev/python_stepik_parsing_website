import requests

response = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')  # get-запрос
s = response.text.encode("utf-8")
s = str(s)
print(s)
