import xlrd

wb = xlrd.open_workbook('salaries.xlsx')

sheet = wb.sheet_by_index(0)
salaries = {}
regs = {}

for i in range(1,sheet.ncols):
    salaries[sheet.col_values(i)[0]] = sum(sheet.col_values(i)[1 : 8]) / sheet.ncols

for i in range(1,sheet.nrows):
    srs = sheet.row_values(i)[1:]
    srs.sort()
    regs[sheet.row_values(i)[0]] = srs[sheet.ncols // 2]

print(max(regs,key=regs.get),max(salaries,key=salaries.get))
#print(salaries.get)
#print(regs)