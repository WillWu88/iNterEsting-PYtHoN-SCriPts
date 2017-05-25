#open workbook
from xlrd import open_workbook
filename = raw_input("What is the name?> ")+".xlsx"
workBook = open_workbook(filename)
sheetNum = input("what's the sheet number?> ")
sheet = workBook.sheet_by_index(sheetNum-1)

#read from the wor sheet
a = []
for cols in range(sheet.nrows):
    for rows in range(sheet.ncols):
        a.insert(len(a),int(sheet.cell_value(rows,cols)))
    print("Now a is:"+str(a))
    next_col = raw_input("Next Roll?> ")
    if (next_col=="no"):
        break
print ("that's all the datas.The following is the a")
print a
