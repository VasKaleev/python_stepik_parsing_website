#coding: cp1251
import xlrd, xlwt
#открываем файл
rb = xlrd.open_workbook('salaries.xlsx')

#выбираем активный лист
sheet = rb.sheet_by_index(0)
val = sheet.row_values(0)[0]
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
print(vals)