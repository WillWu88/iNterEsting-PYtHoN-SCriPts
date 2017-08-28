#open workbook
from xlrd import open_workbook
filename = raw_input("What is the name?> ")+".xlsx"
workBook = open_workbook(filename)
sheetNum = input("what's the sheet number?> ")
sheet = workBook.sheet_by_index(sheetNum-1)

#for debug
#print (sheet.nrows)
#print (sheet.ncols)


a = []

#read from the work sheet and copy the data into an array
print (sheet.cell_value(5,0))
for cols in range(sheet.ncols):
    a = []
    for rows in range(sheet.nrows):
        a.append(str(sheet.cell_value(rows,cols)))
    print ("the function is:"+a[0]+"u^5"+"+"+a[1]+"u^4"+"+"+a[2]+"u^3"+"+"+a[3]+"u^2"+"+"+a[4]+"u^1"+"+"+a[5])
    next_Stat = raw_input("Next? > ")
    if (next_Stat=="no"):
        break
