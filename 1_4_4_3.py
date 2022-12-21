from bs4 import BeautifulSoup as BF
from urllib.request import urlopen, urlretrieve
import re
#import pandas as pd

html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read().decode('utf-8')
webpage = str(html)
regex = ('<td>(.*?)</td>')
l = re.findall(regex, webpage)
print(l)
#data = pd.DataFrame(l, dtype='int')
#data.sum()