import xlrd
wb = xlrd.open_workbook('trekking1.xlsx')

sheet = wb.sheet_by_index(0)
sortm = {}
sortm1 = {}
for i in range(1,sheet.nrows):
    s=sheet.row_values(i)[0:2]
    sortm[sheet.row_values(i)[0]]=sheet.row_values(i)[1]
sortm1=sorted(sortm.items(), key=lambda item: item[1],reverse=True)
for i in range(len(sortm1)):
    print(sortm1[i][0])
