from bs4 import BeautifulSoup
with open("1.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.code)
    print(soup.a)
    print(soup.li)