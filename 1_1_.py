import requests
response = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')  # get-запрос
s = response.text
s = str(s)
print(s)
