#!/usr/bin/env python3
print("Content-type: text/html")
print()
print("<html>")
print("<body>")
print("<table>")
#Формирование таблицы двойным циклом
print("<tr>")
for i in range(1,10):
      print("<td>",i,'</td>',sep=" ")
print("</tr>")
    #<tr>
    #  <td>3</td>
    #  <td>4</td>
print("</table>")
print("</body>")
print("</html>")
