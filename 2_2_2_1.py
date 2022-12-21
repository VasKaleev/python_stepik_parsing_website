import xlrd, xlwt
import statistics
rb = xlrd.open_workbook('salaries.xlsx')
sheet = rb.sheet_by_index(0)
a0 = []
b = []
for rownum in range(1, 9):
    a = []
    temp = sheet.row_values(rownum)
    for i in temp:
        if type(i)==str:
            a0.append(i)
        if type(i)!=str:
            a.append(i)
    b.append(statistics.median(a))
dic = dict(zip(a0, b))
#print(dic)
print(*sorted(dic.items(), key=lambda item: item[1],reverse=True))

a2=[]
b1=[]
ncols = sheet.ncols
for i in range(1,ncols):
   a3=[]
   n = sheet.col_values(i)
   #print(n[2])
   for j in n:
       #print(j)
       if type(j) == str:
            a2.append(j)
       if type(j)!=str:
            #print(j)
            a3.append(j)
            #print(a3)
   b1.append(statistics.mean(a3))
#print(a2)
#print(b1)
dic1 = dict(zip(a2, b1))
#print(dic1)
print(*sorted(dic1.items(), key=lambda item: item[1],reverse=True))




