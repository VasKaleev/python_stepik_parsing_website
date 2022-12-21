import xlrd
wb = xlrd.open_workbook('tab.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)

import pandas as pd
wb = pd.read_excel('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
nmin = wb.iloc[6][2]
for rownum in range(7,27):
      temp = wb.iloc[rownum]
      nmin = min(nmin, temp[2])
print(nmin)

import pandas as pd
wb = pd.read_excel('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
print(min(wb.iloc[6, 2], wb.iloc[7:28, 2].min()))
print(pd.show_versions())